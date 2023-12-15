from datetime import datetime, timedelta

from google.oauth2 import service_account
from googleapiclient.discovery import build

from constants import Constants, PrivateData
from utils import get_cost, is_in_price


class GoogleCalendar:
    def __init__(self):
        self.credentials = (
            service_account.Credentials.from_service_account_file(
                filename=PrivateData.FILE_PATH, scopes=PrivateData.SCOPES
            )
        )
        self.service = build(
            "calendar",
            "v3",
            credentials=self.credentials,
        )

    def __get_calendar(self) -> dict:
        """Возвращает список календарей."""
        return self.service.calendarList().list().execute()

    def __add_calendar(self, calendar_id: str) -> dict:
        """Добавляет календарь служебному аккаунту пользователя."""
        calendar_list_entry = {"id": calendar_id}
        return (
            self.service.calendarList()
            .insert(body=calendar_list_entry)
            .execute()
        )

    def _get_events(
        self, time_from: datetime, time_to: datetime, page_token: str
    ) -> dict:
        """Возвращает список всех занятий со всеми полями."""
        return (
            self.service.events()
            .list(
                calendarId=PrivateData.CALENDAR_ID,
                singleEvents=True,
                pageToken=page_token,
                maxResults=250,
                timeMin=time_from.isoformat() + "Z",
                timeMax=time_to.isoformat() + "Z",
                timeZone="Europe/Moscow",
            )
            .execute()
        )

    def _get_data(
        self,
        time_from: datetime,
        time_to: datetime,
    ) -> list[dict]:
        """Возвращает список всех занятий с нужными полями

        Начало занятия, конец занятия, название.
        Args:
            time_from: Начало занятия.
            time_to: Конец занятия.
        Returns:
            Список словарей с данными занятий.

        """
        my_event = []
        page_token = None
        while True:
            events = self._get_events(time_from, time_to, page_token)
            page_token = events.get("nextPageToken")
            my_events = events.get("items", [])

            for event in my_events:
                name = event.get("summary", "")
                if name and name[0].isalpha() and is_in_price(name):
                    start = event.get("start", {}).get("dateTime", "")
                    end = event.get("end", {}).get("dateTime", "")
                    data_event = {
                        "summary": name,
                        "start": start,
                        "end": end,
                    }
                    my_event.append(data_event)
            if not page_token:
                break
        return my_event

    def formatted_data(
        self,
        date_from=datetime.now() - timedelta(days=Constants.DAYS_TO_PLOT),
        date_to=datetime.now(),
    ) -> dict[datetime.date, int]:
        """Возвращает словарь с датами и доходами."""

        many_days = {}
        data = self._get_data(date_from, date_to)
        for value in data:
            start = datetime.fromisoformat(value.get("start", "")).date()
            many_days[start] = many_days.get(start, 0) + get_cost(
                value.get("summary")
            )

            if start.weekday() == 5:
                many_days[start + timedelta(days=1)] = 0

        return many_days

    def to_message(
        self,
        date_from: datetime,
        date_to: datetime,
    ) -> str:
        """Возвращает сумму доходов."""
        return str(sum(self.formatted_data(date_from, date_to).values()))

from datetime import datetime, timedelta

from google.oauth2 import service_account
from googleapiclient.discovery import build
from icecream import ic

from constants import PrivateData, Constants
from utils import is_in_price, get_cost


class GoogleCalendar:

    def __init__(self):
        self.bablo = []
        credentials = service_account.Credentials.from_service_account_file(
            filename=PrivateData.FILE_PATH, scopes=PrivateData.SCOPES
        )
        ic(PrivateData.FILE_PATH)
        self.service = build("calendar", "v3", credentials=credentials)
        ic()
    def __get_calendar(self):
        return self.service.calendarList().list().execute()

    def __add_calendar(self, calendar_id):
        calendar_list_entry = {
            'id': calendar_id
        }
        return self.service.calendarList().insert(
            body=calendar_list_entry).execute()

    def _get_events(self, time_from, time_to, page_token) -> dict:
        return self.service.events().list(
            calendarId="kamanchi22@gmail.com",
            singleEvents=True,
            pageToken=page_token,
            maxResults=250,
            timeMin=time_from.isoformat() + "Z",
            timeMax=time_to.isoformat() + "Z",
            timeZone="Europe/Moscow",
        ).execute()

    def _get_data(self, time_from: datetime, time_to: datetime) -> list[dict]:
        my_event = []
        ic()
        page_token = None
        while True:
            events = self._get_events(time_from, time_to, page_token=page_token)
            ic()
            page_token = events.get('nextPageToken')
            my_events = events.get('items', [])

            for event in my_events:
                name = event.get('summary', "")
                if name[0].isdigit() or not is_in_price(name):
                    continue
                start = event.get('start', {}).get('dateTime', ""),
                end = event.get('end', {}).get('dateTime', ""),
                data_event = {
                    'summary': name,
                    'start': start,
                    'end': end,
                }
                my_event.append(data_event)
            if not page_token:
                break
        return my_event

    def formatted_data(self, date_from=datetime.now() - timedelta(days=Constants.DAYS_TO_PLOT),
                       date_to=datetime.now(), ):
        many_days = {}
        data = self._get_data(date_from, date_to)
        for value in data:
            start = datetime.fromisoformat(value.get("start", [])[0]).date()
            if start in many_days:
                many_days[start] += get_cost(value.get("summary"))
            else:
                many_days[start] = get_cost(value.get("summary"))
            if start.weekday() == 5:
                many_days[start + timedelta(days=1)] = 0
        return many_days

    def to_message(self, date_from, date_to):
        return sum(self.formatted_data(date_from, date_to).values())

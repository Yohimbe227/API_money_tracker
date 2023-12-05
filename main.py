from datetime import datetime, timedelta

from google.oauth2 import service_account
from googleapiclient.discovery import build
from icecream import ic

from price import Price
from utils import get_datetime, is_in_price, get_cost


class GoogleCalendar:
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    FILE_PATH = "key.json"

    def __init__(self):
        self.bablo = []
        credentials = service_account.Credentials.from_service_account_file(
            filename=GoogleCalendar.FILE_PATH, scopes=GoogleCalendar.SCOPES
        )
        self.service = build("calendar", "v3", credentials=credentials)

    def __get_calendar(self):
        return self.service.calendarList().list().execute()

    def __add_calendar(self, calendar_id):
        calendar_list_entry = {
            'id': calendar_id
        }
        return self.service.calendarList().insert(
            body=calendar_list_entry).execute()

    def _get_data(self, time_from, time_to) -> list[dict]:
        page_token = None
        my_event = []
        while True:
            events = self.service.events().list(
                calendarId="kamanchi22@gmail.com",
                singleEvents=True,
                pageToken=page_token,
                maxResults=250,
                timeMin=time_from,
                timeMax=time_to,
                timeZone="Europe/Moscow",
            ).execute()
            page_token = events.get('nextPageToken')
            my_events = events.get('items', [])

            for event in my_events:
                name = event.get('summary', "")
                if name[0].isdigit():
                    continue
                if not is_in_price(name):
                    continue
                start = event.get('start', {}).get('dateTime', ""),
                end = event.get('end', {}).get('dateTime', "")[0],
                data_event = {
                    'summary': name,
                    'start': start,
                    'end': end,
                }
                my_event.append(data_event)
            if not page_token:
                break
        return my_event

    def formatted_data(self, date_from=datetime.now() - timedelta(days=30),
                       date_to=datetime.now(), ):
        many_days = {}
        data = self._get_data(date_from, date_to)
        for value in data:
            start = datetime.fromisoformat(value.get("start"))
            if start in many_days:
                many_days[start] += get_cost(value.get("summary"))
            else:
                many_days[start] = get_cost(value.get("summary"))

            ic(many_days)

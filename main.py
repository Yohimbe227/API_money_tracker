import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from icecream import ic

from price import Price
from utils import get_datetime, is_in_price, get_cost


class GoogleCalendar:
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    FILE_PATH = "key.json"

    def __init__(self):
        self.bablo = 0
        credentials = service_account.Credentials.from_service_account_file(
            filename=GoogleCalendar.FILE_PATH, scopes=GoogleCalendar.SCOPES
        )
        self.service = build("calendar", "v3", credentials=credentials)

    def get_calendar(self):
        return self.service.calendarList().list().execute()

    def add_calendar(self, calendar_id):
        calendar_list_entry = {
            'id': calendar_id
        }
        return self.service.calendarList().insert(
            body=calendar_list_entry).execute()

    def list_calendars(self, time_from, time_to) -> str:
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
                if is_in_price(name):
                    self.bablo += get_cost(name)
                data_event = {
                    'summary': name,
                    'start': event.get('start', {}).get('dateTime', ""),
                    'end': event.get('end', {}).get('dateTime', ""),
                }
                my_event.append(data_event)
            if not page_token:
                break
        return str(self.bablo)

import asyncio
import datetime
import os

from dotenv import load_dotenv
from icecream import ic

from main import GoogleCalendar
import requests


load_dotenv()


def main():
    obj = GoogleCalendar()
    date_to = datetime.datetime.now()

    if datetime.datetime.now().weekday() < 6:
        delta_time = datetime.timedelta(days=1)
        date_from = date_to - delta_time
        result = obj.list_calendars(
            date_from.isoformat() + "Z",
            date_to.isoformat() + "Z",
        ),
    elif datetime.datetime.now().weekday() == 7:
        delta_time = datetime.timedelta(days=7)
        date_from = date_to - delta_time
        result = obj.list_calendars(
            date_from.isoformat() + "Z",
            date_to.isoformat() + "Z",
        ),
    else:
        result = 'Сегодня выходной'

    bot_token = os.getenv("TELEGRAM_TOKEN")
    if bot_token is None:
        return
    chat_id = os.getenv("TELEGRAM_TO")
    api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': result
    }

    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        print('Сообщение успешно отправлено.')
    else:
        print('Ошибка отправки сообщения:', response.text)


if __name__ == "__main__":
    main()

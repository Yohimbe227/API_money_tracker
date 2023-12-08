import os
from http import HTTPStatus

from dotenv import load_dotenv
from datetime import datetime, timedelta

from constants import Constants
from dashboard import Plot
from exceptions import TokenError
from main import GoogleCalendar
import requests


load_dotenv()

calendar = GoogleCalendar()


bot_token = os.getenv("TELEGRAM_TOKEN")
if bot_token is None:
    raise TokenError(bot_token)

chat_id = os.getenv("TELEGRAM_TO")
api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
payload = {
    'chat_id': chat_id,
    'text': calendar.to_message(datetime.now() - timedelta(days=Constants.DAYS_TO_MESSAGE), datetime.now()),
}

diagram = Plot(
    date_from=datetime.now() - timedelta(days=Constants.DAYS_TO_PLOT),
    date_to=datetime.now(),
    bablo=calendar.formatted_data(),
)
diagram.show_diagram()

response = requests.post(api_url, json=payload)

if response.status_code == HTTPStatus.OK:
    print('Сообщение успешно отправлено.')
else:
    print('Ошибка отправки сообщения:', response.text)


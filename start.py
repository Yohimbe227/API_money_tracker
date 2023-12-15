import os
from datetime import datetime, timedelta
from http import HTTPStatus

import requests
from dotenv import load_dotenv

from constants import Constants, PrivateData
from dashboard import Plot
from mycalendar import GoogleCalendar
from utils import logger

load_dotenv("infra/.env.calendar")

calendar = GoogleCalendar()


api_url = f"https://api.telegram.org/bot{PrivateData.TELEGRAM_TOKEN}/sendMessage"
payload = {
    "chat_id": int(PrivateData.ID),
    "text": calendar.to_message(
        datetime.now() - timedelta(days=Constants.DAYS_TO_MESSAGE),
        datetime.now(),
    ),
}

diagram = Plot(
    date_from=datetime.now() - timedelta(days=Constants.DAYS_TO_PLOT),
    date_to=datetime.now(),
    bablo=calendar.formatted_data(),
)
diagram.show_diagram()

response = requests.post(api_url, json=payload)

if response.status_code == HTTPStatus.OK:
    logger.info("Сообщение отправлено.")
else:
    logger.critical("Сообщение не отправлено.")

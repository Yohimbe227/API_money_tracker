import os

from dotenv import load_dotenv
from datetime import datetime, timedelta

from bokeh.plotting import figure, output_file, show
from icecream import ic

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
    'text': calendar.formatted_data(),
}
ic(payload)
output_file("graph.html")

diagram = Plot(
    datetime.now() - timedelta(days=30),
    datetime.now(),
    bablo=calendar.formatted_data()[0],
)
diagram.show_diagram()

show(diagram.diagram)
response = requests.post(api_url, json=payload)

if response.status_code == 200:
    print('Сообщение успешно отправлено.')
else:
    print('Ошибка отправки сообщения:', response.text)

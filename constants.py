import os

from dotenv import load_dotenv

load_dotenv('.env.calendar')


class PrivateData:
    def __setattr__(self, key, value):
        raise AttributeError(f"can't reassign constant '{value}'")

    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    ID = int(os.getenv("TELEGRAM_TO"))
    SCOPES = [os.getenv("SCOPES")]
    FILE_PATH = os.getenv("FILE_PATH")
    CALENDAR_ID = os.getenv("CALENDAR_ID")


class Constants:
    def __setattr__(self, key, value):
        raise AttributeError(f"can't reassign constant '{value}'")

    COST = {
        "Никита": 1200,
        "Соня": 1200,
        "Артем": 1200,
        "Эльвира": 1300,
        "Василат": 1300,
        "Александр": 1400,
        "Михаил": 1300,
        "Настя": 1300,
        "Федор": 1400,
        "Даниил": 2200,
        "Святослав": 2200,
        "Влад": 1900,
    }

    WEEKDAYS = {0: "Пн", 1: "Вт", 2: "Ср", 3: "Чт", 4: "Пт", 5: "Сб", 6: "Вс"}
    DAYS_TO_MESSAGE = 7
    DAYS_TO_PLOT = 30
    MAX_INCOME = 6000

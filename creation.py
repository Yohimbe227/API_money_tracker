from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from costants import TELEGRAM_TOKEN
from utils import check_tokens


storage = MemoryStorage()
check_tokens(TELEGRAM_TOKEN)
bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(storage=storage)

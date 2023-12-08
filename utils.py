import datetime
import logging

from icecream import ic

from constants import Constants
from exceptions import TokenError

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s, %(levelname)s, %(message)s, %(funcName)s",
)
logger = logging.getLogger(__name__)


def is_in_price(name: str | None) -> bool:
    """Check if name is in price

        Args:
            name: Name of event.
    """
    if name is None:
        return False
    for key, value in Constants.COST.items():
        if name.lower().startswith(key.lower()):
            return True


def get_datetime(year: int, month: int, day: int) -> str:
    """
    Преобразует год, месяц и день в формат ISO формате.

    Args:
        year: Год.
        month: Месяц.
        day: День.

    Returns:
        Время в формате ISO.

    """
    return datetime.datetime(year, month, day,).isoformat() + "Z"


def get_cost(name: str | None) -> int:
    """Возвращает стоимость события по его имени.

        Args:
            name: Имя события.

        Raises:
            AttributeError: Нет такого клиента в списке.

        Returns:
            Стоимость события.

    """
    if name is None:
        raise AttributeError("Не передано имя клиента..")
    for key, value in Constants.COST.items():
        if name.lower().startswith(key.lower()):
            return Constants.COST.get(key)
    raise AttributeError("Нет такого клиента в списке.")


def check_tokens(token) -> None:
    """Доступность токенов в переменных окружения.

    Args:
        token: Токен телеграм бота.

    Raises:
        TokenError: Отсутствует какой-либо из необходимых токенов.

    """
    notoken = "TELEGRAM_TOKEN" if token is None else None
    if notoken:
        logger.critical("Необходимый токен: %s не обнаружен", notoken)
        raise TokenError(notoken)

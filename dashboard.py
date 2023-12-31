from datetime import datetime

from bokeh.io import save
from bokeh.plotting import figure, output_file

from constants import Constants


class Plot:
    """
    Класс для построения диаграммы.

    Attributes:
        date_from: Начальная дата.
        date_to: Конечная дата.
        bablo: Словарь с датами и доходами.
        height: Высота диаграммы.
    """

    def __init__(
        self,
        date_from: datetime,
        date_to: datetime,
        bablo: dict[datetime, int],
        height: int = 550,
    ):
        self.date_from = date_from
        self.date_to = date_to
        self.height = height
        self.bablo = dict(sorted(bablo.items()))

    def _get_days(self) -> list[str]:
        """Возвращает список дат.

        Returns:
            Список дат.
        """
        return [
            str(day.month)
            + "-"
            + str(day.day)
            + " \n"
            + Constants.WEEKDAYS[day.weekday()]
            for day in self.bablo.keys()
        ]

    def _get_many(self):
        """Возвращает список сумм.

        Returns:
            Список сумм.
        """
        return list(self.bablo.values())

    def show_diagram(self):
        """Сохраняет диаграмму."""
        diagram = self.create_diagram()
        diagram.vbar(
            x=self._get_days(),
            top=self._get_many(),
            width=0.8,
            color="green",
        )
        save(diagram)

    def create_diagram(self):
        """Создает диаграмму."""
        output_file("diagram/diagram.html", title="Динамика доходов за месяц")
        diagram = figure(
            x_range=self._get_days(),
            height=self.height,
            title="Динамика доходов",
            width=self.height * 3,
            sizing_mode="scale_width",
        )
        diagram.title.align = "center"
        diagram.y_range.bounds = (0, Constants.MAX_INCOME)
        diagram.xaxis.axis_label = 'Дата'
        diagram.yaxis.axis_label = 'Доход, руб.'
        diagram.title.text_font_size = "20pt"
        diagram.xaxis.axis_label_text_font_size = "16pt"
        diagram.yaxis.axis_label_text_font_size = "16pt"
        return diagram


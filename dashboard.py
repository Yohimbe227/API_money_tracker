from datetime import datetime, timedelta

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, DatetimeTickFormatter, Range1d, \
    LinearAxis, FuncTickFormatter
from icecream import ic

from price import WEEKDAYS


class Plot:
    """
    Класс для построения диаграммы.

    Attributes:
        date_from: Начальная дата.
        date_to: Конечная дата.
        bablo: Словарь с датами и доходами.
        height: Высота диаграммы.
    """

    def __init__(self, date_from: datetime, date_to: datetime,
                 bablo: dict[datetime, int], height: int = 550, ):
        self.date_from = date_from
        self.date_to = date_to
        self.height = height
        self.bablo = dict(sorted(bablo.items()))

    def _get_days(self) -> list[str]:
        """Возвращает список дат.

        Returns:
            Список дат.
        """
        return [str(day.month) + "-" + str(day.day) + " \n" + WEEKDAYS[
            day.weekday()] for day in
                self.bablo.keys()]

    def _get_many(self):
        """Возвращает список сумм.

        Returns:
            Список сумм.
        """
        return list(self.bablo.values())

    def show_diagram(self):
        """Создает и показывает диаграмму."""
        output_file("diagram.html")
        diagram = figure(
            x_range=self._get_days(),
            height=self.height,
            title="Динамика доходов",
            width=self.height * 3,
            sizing_mode="scale_width",
        )
        ic(self._get_days())
        diagram.y_range.bounds = (0, 6000)
        diagram.xaxis.axis_label = 'Дата'
        diagram.yaxis.axis_label = 'Доход'
        diagram.title.text_font_size = "20pt"
        diagram.xaxis.axis_label_text_font_size = "16pt"
        diagram.yaxis.axis_label_text_font_size = "16pt"
        source = ColumnDataSource(
            data=dict(x=self._get_days(), y=self._get_many()))
        diagram.vbar(x=self._get_days(), top=self._get_many(), width=0.5,
                     color="green",
                     )

        show(diagram)

# widgets.interact(obj.update, days=(1, 5))
# curdoc().add_root(obj.diagram)

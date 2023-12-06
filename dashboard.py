from datetime import datetime, timedelta

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from icecream import ic


class Plot:
    def __init__(self, date_from: datetime, date_to: datetime,
                 bablo: dict[datetime, int], height: int = 550, ):
        self.date_from = date_from
        self.date_to = date_to
        self.height = height
        self.bablo = bablo

    def _get_days(self):
        return [datetime.combine(d, datetime.min.time()) for d in
                self.bablo.keys()]

    def _get_many(self):
        return list(self.bablo.values())

    # def update(self, ):
    #     self.source = ColumnDataSource(data=dict(x=self._get_days(), y=self._get_many()))

    def show_diagram(self):
        diagram = figure(
            height=self.height,
            title="Динамика доходов",
            width=self.height * 3,
            sizing_mode="scale_width",
            x_axis_type="datetime",
        )
        diagram.y_range.bounds = (0, 6000)
        diagram.xaxis.axis_label = 'Дата'
        diagram.yaxis.axis_label = 'Доход'
        source = ColumnDataSource(
            data=dict(x=self._get_days(), y=self._get_many()))
        diagram.vbar(x='x', top='y', color="green", width=timedelta(hours=20),
                     source=source)
        show(diagram)

# widgets.interact(obj.update, days=(1, 5))
# curdoc().add_root(obj.diagram)

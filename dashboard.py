from datetime import datetime, timedelta

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource


class Plot:
    def __init__(self, date_from, date_to, bablo, height=550):
        self.date_from = date_from
        self.date_to = date_to
        self.height = height
        self.diagram = figure(x_range=(self.date_from, self.date_to),
                              height=self.height,
                              title="Динамика доходов",
                              width=self.height*3,
                              sizing_mode="scale_width"
                              )
        self.diagram.y_range.bounds = (0, 6000)
        self.diagram.xaxis.axis_label = 'Дата'
        self.diagram.yaxis.axis_label = 'Доход'
        self.ys = bablo
        self.source = ColumnDataSource(data=dict(x=self.get_days(), y=self.ys))

    def get_days(self):
        delta = timedelta(days=1)
        date_from = self.date_from
        date_to = self.date_to
        days = []
        while date_from <= date_to:
            days.append(date_from)
            date_from += delta
        return days

    def update(self, ):
        self.source = ColumnDataSource(data=dict(x=self.get_days(), y=self.ys))

    def show_diagram(self):
        self.diagram.xaxis.axis_label = 'Дата'
        self.diagram.yaxis.axis_label = 'Доход'
        self.diagram.vbar(x='x', top='y', width=timedelta(hours=20), color="green",
                          source=self.source)
        self.diagram.xgrid.grid_line_color = None



# widgets.interact(obj.update, days=(1, 5))
# curdoc().add_root(obj.diagram)

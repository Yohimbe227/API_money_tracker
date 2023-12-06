from datetime import datetime, timedelta

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from icecream import ic


class Plot:
    def __init__(self, date_from, date_to, bablo, height=550):
        self.date_from = date_from
        self.date_to = date_to
        self.height = height
        self.diagram = figure(x_range=[self.date_from, self.date_to],
                              height=self.height,
                              title="Динамика доходов",
                              width=self.height*3,
                              sizing_mode="scale_width",
                              x_axis_type="datetime"
                              )
        self.diagram.y_range.bounds = (0, 6000)
        self.diagram.xaxis.axis_label = 'Дата'
        self.diagram.yaxis.axis_label = 'Доход'
        self.bablo = bablo
        # self.source = ColumnDataSource(data=dict(x=list(self.bablo.keys()), y=list(self.bablo.values())))

    def _get_days(self):
        return list( self.bablo.keys())

    def _get_many(self):
        return list(self.bablo.values())

    # def update(self, ):
    #     self.source = ColumnDataSource(data=dict(x=self._get_days(), y=self._get_many()))

    def show_diagram(self):

        source = ColumnDataSource(data=dict(x=self._get_days(), y=self._get_many()))
        # ic(source.data)

        self.diagram.xaxis.axis_label = 'Дата'
        self.diagram.yaxis.axis_label = 'Доход'
        self.diagram.vbar(data=source.data, color="green",
                          )
        self.diagram.xgrid.grid_line_color = None
        show(self.diagram)



# widgets.interact(obj.update, days=(1, 5))
# curdoc().add_root(obj.diagram)

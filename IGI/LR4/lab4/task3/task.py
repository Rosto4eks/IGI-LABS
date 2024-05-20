from .series import *


class Task3:
    def __init__(self):
        print("TASK 3: draw plots and calculate statistic data\n")
        s = SeriesTask(100, 1e-4)
        s.calculate()
        s.plot()
        return

from .matrix import *


class Task5:
    def __init__(self):
        print("TASK 5: count odd and even elements in array and calculate correlation coefficient\n")
        m = Matrix(6, 6)
        print(m.get())
        odd, even = m.OddandEvenCount()
        print(f"odd: {odd}, even: {even}")
        print(f"correlation coefficient: {m.Corr()}")
        return

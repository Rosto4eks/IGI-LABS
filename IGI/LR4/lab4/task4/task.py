from .lib import *
from .input import *

class Task4:
    def __init__(self):
        print("TASK 4: create geometric classes and plot figures\n")
        correct = False
        while (not correct):
            print("Input baseline length\n")
            n = inputInt()
            print("Input midline length")
            m = inputInt()
            print("Input height")
            h = inputInt()
            color = input("Input color: ")
            name = input("Input name: ")
            if n <= 0 or m >= n or h <= 0 or m < n // 2:
                print("Incorrect input, try again")
            elif color != "red" and color != "blue" and color != "yellow" and color != "green":
                print("Incorrect input, try again")
            else:
                correct = True
        self._trapeze = Trapeze(n, m, h, color, name)

    
    def start(self):
        print('--- select action ---\n \
               1 - get data\n \
               2 - plot\n \
               3 - back\n')
        inp = inputInt()

        match inp:
            case 1:
                print(self._trapeze.info())
            case 2:
                self._trapeze.plot()
            case 3:
                return
            
        self.start()


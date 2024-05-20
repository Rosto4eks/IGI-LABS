from task1.task import *
from task1.input import *
from task2.task import *
from task3.task import *
from task4.task import *
from task5.task import *
from task6.task import *

class Main:
    def __init__(self):
        print("SERGEEV R.V. 253502 19 VARIANT")


    def start(self):
        print('--- select action ---\n \
               1 - TASK 1\n \
               2 - TASK 2\n \
               3 - TASK 3\n \
               4 - TASK 4\n \
               5 - TASK 5\n \
               6 - TASK 6\n \
               7 - exit\n')
        inp = inputInt()

        match inp:
            case 1:
                Task1().start()
            case 2:
                Task2().start()
            case 3:
                Task3()
            case 4:
                Task4().start()
            case 5:
                Task5()
            case 6:
                Task6()
            case 7:
                return
            
        self.start()


Main().start()
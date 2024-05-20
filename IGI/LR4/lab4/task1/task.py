from .classroom import *
from .serializer import *
from .input import *

class Task1:
    def __init__(self):
        print("TASK 1: serialize data, read, search and sort it\n")
        self._classroom = ClassRoom([Student("Shishka", 14, 5, 2004), Student("Bekar", 3, 9, 2004), Student("Googlis", 27, 12, 2005), Student("Foreach", 19, 7, 2004)])


    def start(self):
        print('--- select action ---\n \
               1 - print classroom\n \
               2 - sort classroom\n \
               3 - get average date\n \
               4 - get student info by name\n \
               5 - save to csv\n \
               6 - save to pickle\n \
               7 - back\n')
        inp = inputInt()

        match inp:
            case 1:
                [print(c) for c in self._classroom._students]
            case 2:
                self._classroom.sort()
            case 3:
                print(self._classroom.avg_date())
            case 4:
                print(self._classroom.find_by_name(input("write student name:")))
            case 5:
                Serializer.to_csv(self._classroom, input("write filename: "))
            case 6:
                Serializer.to_pickle(self._classroom, input("write filename: "))
            case 7:
                return
            
        self.start()

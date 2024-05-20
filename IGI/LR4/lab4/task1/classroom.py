from .student import *

class ClassRoom:
    sort_fn = lambda s: s.name

    def __init__(self, students: list[Student]) -> tuple[int, int, int]:
        self._students = students
    
    def avg_date(self) -> tuple[int, int, int]:
        '''
        return average day, month and year of the class
        '''
        avg_day = 0
        avg_month = 0 
        avg_year = 0

        for student in self._students:
            avg_day += student.day
            avg_month += student.month
            avg_year += student.year

        avg_day //= len(self._students)
        avg_month //= len(self._students)
        avg_year //= len(self._students)

        return avg_day, avg_month, avg_year
    

    def sort(self):
        '''
        sorts class by name
        '''
        self._students.sort(key=ClassRoom.sort_fn)


    def find_by_name(self, name: str) -> Student:
        '''
        return student if exists, else return null
        '''
        for s in self._students:
            if s.name == name:
                return s
        return None
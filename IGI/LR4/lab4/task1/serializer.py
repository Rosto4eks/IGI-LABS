import csv
import pickle
from .classroom import *

class Serializer:
    @staticmethod
    def to_csv(classroom: ClassRoom, filename: str):
        """
        Static method for converting list of students to *.csv file
        """
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'day', 'month', 'year']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in  classroom._students:
                writer.writerow({'name': student.name,
                             'day': student.day,
                             'month': student.month,
                             'year': student.year})
            
    @staticmethod
    def to_pickle(classroom: ClassRoom, filename: str):
        """
        Serialize list of students to *.pkl file.
        """
        with open(filename, 'wb') as picklefile:
            pickle.dump(classroom._students, picklefile)

    @staticmethod
    def from_csv(filename: str) -> ClassRoom:
        """
        Load students from *.csv file.
        """
        students = []
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(Student(row['name'], int(row['day']), int(row['month']), int(row['year'])))
        return ClassRoom(students)
    
    @staticmethod
    def from_pickle(filename: str) -> ClassRoom:
        """
        Load students from *.pkl file.
        """
        with open(filename, 'rb') as picklefile:
            students: list[Student] = pickle.load(picklefile)
            return ClassRoom(students)


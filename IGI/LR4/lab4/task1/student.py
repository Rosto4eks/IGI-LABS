class Date:
    def __init__(self, day : int, month : int, year : int):
        self.day = day
        self.month = month
        self.year = year


class PrintMixin:
    def print_info(self) -> None:
        """
        Get full info about student.
        """
        print(f"Name: {self.name}, Date of birth: {str(self.day).zfill(2)}.{str(self.month).zfill(2)}.{str(self.year).zfill(4)}")


class Student(Date, PrintMixin):
    def __init__(self, name : str, day : int, month : int, year : int):
        super().__init__(day, month, year)
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} : {self.day}.{self.month}.{self.year}"
        

    @property
    def birth_date(self):
        """
        Property of birthday.
        """
        return self.year, self.month, self.day
    
    @birth_date.setter
    def birth_date(self, value : tuple[int, int, int]):
        """
        Setter of birthday.
        """
        if value.__sizeof__() < 3:
            raise ValueError("Wrong format of date!")
        self.day = value[2]
        self.month = value[1]
        self.year = value[0]
        
    
    
        
        
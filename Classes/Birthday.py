from .Field import Field
from datetime import datetime

class Birthday(Field):
    def __init__(self, value):
        self.birthdate = self.__str_to_date(value)
        
    
    def __str_to_date(self, value):
        try:
            return datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
from .Field import Field
from datetime import datetime
import re

class Birthday(Field):
    def __init__(self, value):
        pattern = r"^\d{2}\.\d{2}\.\d{4}$"
        if not re.match(pattern, value):
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
        super().__init__(value)
        

    def __str__(self):
        return self.value
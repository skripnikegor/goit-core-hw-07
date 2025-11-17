from .Field import Field
from datetime import datetime
import re

class Birthday(Field):
    def __init__(self, value):
        pattern = r"^\d{2}\.\d{2}\.\d{4}$"
        if re.match(pattern, value):
            super().__init__(self.value)
        else:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        

    def __str__(self):
        return self.value
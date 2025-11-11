from .Field import Field
from datetime import datetime

class Birthday(Field):
    def __init__(self, value):
        try:
            date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(date)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")
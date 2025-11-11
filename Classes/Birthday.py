from Field import Field

class Birthday(Field):
    def __init__(self, value):
        try:
            pass
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
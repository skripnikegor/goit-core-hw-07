import re
from Field import Field

class Phone(Field):
    def __init__(self, value):
        if self.__validate_number(value):
            super().__init__(value)
        else:
             raise ValueError("The number should be 10 integers")

    def __validate_number(self, phone_number):
        pattern = r'^\d{10}$'
        return bool(re.match(pattern, phone_number))
    
    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        if isinstance(other, str):
            return self.value == other
        return False
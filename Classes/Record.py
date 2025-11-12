from .Name import Name
from .Phone import Phone
from .Birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, new_phone: Phone):
        new_phone = Phone(new_phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone_number: Phone):
        phone = self.find_phone(phone_number)
        self.phones.remove(phone)

    
    def edit_phone(self, old_number, new_number) -> bool:
        old_phone = self.find_phone(old_number)
        new_phone = Phone(new_number)
        
        if old_phone and new_phone:
            self.remove_phone(old_phone)
            self.add_phone(new_number)
                 
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone_number == phone:
                return phone
        else:
            raise ValueError(f"Can not find {phone_number} in the phone book.")
        
    def add_birthday(self, birthday_date: str):
        if self.birthday:
            return "Birthday alredy defined"
        birthday = Birthday(birthday_date)
        self.birthday = birthday

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
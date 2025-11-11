from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

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

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, new_phone: Phone):
        new_phone = Phone(new_phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone_number: Phone):
        phone = self.find_phone(phone_number)
        self.phones.remove(phone)

    
    def edit_phone(self, old_number, new_number):
        phone = self.find_phone(old_number)
        if phone:
            self.remove_phone(phone)
            self.add_phone(new_number)
                 
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone_number == phone:
                return phone
        else:
            raise ValueError(f"Can not find {phone_number} in the phone book")

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def add_record(self, record: Record):
           self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
         self.data.pop(name, None)

    def __str__(self):
        return ", ".join(f"{key}: {value}" for key, value in self.data.items())
            




book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
    
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")

john.edit_phone("1234567890", "1112223333")



print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

print(book.__str__())

# Видалення запису Jane
book.delete("Jane")


john.edit_phone("1234567890", "1112223333")
print(john)
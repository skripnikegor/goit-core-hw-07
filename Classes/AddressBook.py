from collections import UserDict
from Record import Record

class AddressBook(UserDict):
    
    def add_record(self, record: Record):
           self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
         self.data.pop(name, None)

    def __str__(self):
        return ", ".join(f"{key}: {value}" for key, value in self.data.items())
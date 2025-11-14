from collections import UserDict
from .Record import Record
from datetime import datetime, date, timedelta

class AddressBook(UserDict):
    
    def add_record(self, record: Record):
           self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
         self.data.pop(name, None)

    def __date_to_string(self, date):
        return date.strftime("%d.%m.%Y")
    
    def __find_next_weekday(self, start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    def __adjust_for_weekend(self, birthday):
        if birthday.weekday() >= 5:
            return self.__find_next_weekday(birthday, 0)
        return birthday

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()
        users = self.data.items()

        for user_name, user_data in users:
            try:
                bithday_date = user_data.birthday.value
            except:
                break
            birthday_this_year = bithday_date.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                

            if 0 <= (birthday_this_year - today).days <= days:

                birthday_this_year = self.__adjust_for_weekend(birthday_this_year)

                congratulation_date_str = self.__date_to_string(birthday_this_year)
                upcoming_birthdays.append({"name": user_name, "congratulation_date": congratulation_date_str})
        return upcoming_birthdays

    def __str__(self):
        return "\n".join(f"{key}: {value}" for key, value in self.data.items())
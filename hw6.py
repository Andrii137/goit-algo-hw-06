from collections import UserDict

class Field:
    def __init__(self, value):
        if self.__is_valid(value):
            self.value = value
        else:
            raise ValueError
        
    def __is_valid(value):
        return True

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __is_valid(self, value):
        if len(value)>0:
            return True
        raise ValueError

class Phone(Field):
    def __is_valid(self, value):
        if value.isdigit() and len(value) == 10:
            return True
        raise ValueError

class Record: 
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                self.phones.remove(ph)

    def edit_phone(self, old_phone, new_phone):
        phone_old = Phone(old_phone)
        phone_new = Phone(new_phone)
        self.remove_phone(phone_old.value)
        self.add_phone(phone_new.value)
        if not isinstance(new_phone, str) or len(new_phone) != 10 or not new_phone.isdigit():
            raise ValueError("New phone number must be a string of 10 digits.")

        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return

        raise ValueError("Old phone number not found in record.")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if str(phone) == phone_number:
                return phone
            else:
                return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"
class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name] = record

    def find(self, name):
        for user_name, record in self.data.items():
            if user_name.value == name:
                return record
        return None

    def delete(self, name):
        for user_name, record in self.data.items():
            if user_name.value == name:
                del self.data[record.name]
                break
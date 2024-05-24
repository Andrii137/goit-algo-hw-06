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
    def __init__(self, value):
        if self.__is_valid(value):
            self.value = value
        else:
            raise ValueError

    def __is_valid(self, value):
        if len(value)>0:
            return True
        raise ValueError

class Phone(Field):
    def __init__(self, value):
        if self.__is_valid(value):
            self.value = value
        else:
            raise ValueError

    def __is_valid(self, value):
        if value.isdigit() and len(value) == 10:
            return True
        raise ValueError
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


    def add_phone(self, phone):
        my_phone = Phone(phone)         
        self.phones.append(my_phone)

    def remove_phone(self, phone):
        f = Phone(phone)
        for user_phone in self.phones:
            if user_phone.value == f.value:
                del self.phones[self.phones.index(user_phone)]

    def edit_phone(self, old_phone, new_phone):
        phone_old = Phone(old_phone)
        phone_new = Phone(new_phone)
        self.remove_phone(phone_old.value)
        self.add_phone(phone_new.value)

    def find_phone(self, phone):
        f = Phone(phone)
        for user_phone in self.phones:
            if f.value == user_phone.value:
                return user_phone            
        return None

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
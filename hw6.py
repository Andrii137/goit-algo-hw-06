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
    def __init__(self, phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must have 10 digits.")
        super().__init__(phone)

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
        phone_exists = False
        for p in self.phones:
            if p.value == old_phone:
                phone_exists = True
                break

        if not phone_exists:
            raise ValueError("Phone number to edit does not exist.")

        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("New phone number must be a 10-digit number.")

        for ph in self.phones:
            if ph.value == old_phone:
                ph.value = new_phone

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
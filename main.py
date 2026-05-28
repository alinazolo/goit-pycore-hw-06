from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_to_remove = self.find_phone(phone)

        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError("Phone number not found.")

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.find_phone(old_phone)

        if phone_to_edit:
            phone_to_edit.value = Phone(new_phone).value
        else:
            raise ValueError("Phone number not found.")

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Contact was not found")


book = AddressBook()

# Створюємо контакт
john_record = Record("John")

# Додаємо телефони
john_record.add_phone("1234567890")
john_record.add_phone("0987654321")

# Додаємо контакт в адресну книгу
book.add_record(john_record)

# Виводимо контакт
print(book.find("John"))

# Редагуємо телефон
john_record.edit_phone("1234567890", "1112223333")

print(book.find("John"))

# Шукаємо телефон
found_phone = john_record.find_phone("1112223333")
print(found_phone)

# Видаляємо телефон
john_record.remove_phone("0987654321")

print(book.find("John"))

# Видаляємо контакт
book.delete("John")

from abc import ABC, abstractmethod

class AddressBook(ABC):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    @abstractmethod
    def contact(self):
        pass

class Person(AddressBook):
    def __init__(self, name, address, phone):
        super().__init__(name, address)
        self.phone = phone

    def contact(self):
        return f"{self.name} lives at {self.address}. Contact: {self.phone}"

class Organization(AddressBook):
    def __init__(self, name, address, email):
        super().__init__(name, address)
        self.email = email

    def contact(self):
        return f"{self.name} located at {self.address}. Email: {self.email}"

# Тестуємо реалізацію
person1 = Person("Taras Shevchenko", "Kyiv DniproSt", "555-1234")
org1 = Organization("ABC Inc.", "456 Elm St", "info@shevchenko.com")

print(person1.contact())  # Виведе: Taras Shevchenko lives Kyiv Dnipro St. Contact: 555-1234
print(org1.contact())     # Виведе: ABC Inc. located at 456 Elm St. Email: info@shevchenko.com


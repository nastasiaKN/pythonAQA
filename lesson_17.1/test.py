from faker import Faker

fake = Faker()


class Person:
    def __init__(self):
        self.full_name = fake.name()
        self.gender = fake.random_element(elements=("Male", "Female"))
        self.country = fake.country()
        self.address = fake.address()


person = Person()

print("Full Name:", person.full_name)
print("Gender:", person.gender)
print("Country:", person.country)
print("Address:", person.address)
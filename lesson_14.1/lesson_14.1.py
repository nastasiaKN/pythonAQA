class Student:
    def __init__(self, first_name, last_name, age, avg_marks):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.avg_marks = avg_marks

    def update_avg_marks(self, new_mark):
        self.avg_marks = new_mark

    def __str__(self):
        return (f"Name: {self.first_name}\n"
                f"Last name: {self.last_name}\n"
                f"Age: {self.age}\n"
                f"Average marks: {self.avg_marks}")

if __name__ == "__main__":
    student1 = Student("John", "Doe", 18, 4.2)
    student1.update_avg_marks(4.8)
    print(student1)
class Student:
    def __init__(self, first_name, last_name, age, avg_marks):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.avg_marks = avg_marks

    def update_avg_marks(self, new_mark):
        self.avg_marks = new_mark

    def show_info(self):
        print("Name:", self.first_name)
        print("Last name:", self.last_name)
        print("Age:", self.age)
        print("Average marks:", self.avg_marks)


student1 = Student("John", "Doe", 18, 4.2)

student1.update_avg_marks(4.8)

student1.show_info()
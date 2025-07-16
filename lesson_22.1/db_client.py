from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
from models import Base, Student, Course

class DBClient:
    def __init__(self, db_url="sqlite:///student_system.db"):
        self.engine = create_engine(db_url, echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def seed_courses(self):
        course_names = ["Math", "Physics", "History", "Programming", "Art"]
        courses = [Course(name=name) for name in course_names]
        self.session.add_all(courses)
        self.session.commit()

    def seed_students(self, count=20):
        courses = self.session.query(Course).all()
        for i in range(1, count + 1):
            student = Student(name=f"Student{i}")
            student.courses = random.sample(courses, k=random.randint(1, 3))
            self.session.add(student)
        self.session.commit()

    def add_student(self, name, course_ids):
        new_student = Student(name=name)
        new_student.courses = self.session.query(Course).filter(Course.id.in_(course_ids)).all()
        self.session.add(new_student)
        self.session.commit()
        print(f"Student '{name}' added.")

    def show_students_on_course(self, course_id):
        course = self.session.get(Course, course_id)
        if course:
            print(f"Students on course '{course.name}':")
            for s in course.students:
                print(f"- {s.name}")

    def show_courses_of_student(self, student_id):
        student = self.session.get(Student, student_id)
        if student:
            print(f"Courses of student '{student.name}':")
            for c in student.courses:
                print(f"- {c.name}")

    def update_student_name(self, student_id, new_name):
        student = self.session.get(Student, student_id)
        if student:
            student.name = new_name
            self.session.commit()
            print("Student name updated.")

    def delete_student(self, student_id):
        student = self.session.get(Student, student_id)
        if student:
            self.session.delete(student)
            self.session.commit()
            print("Student deleted.")
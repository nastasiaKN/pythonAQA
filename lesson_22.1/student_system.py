from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

Base = declarative_base()

student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=student_course, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", secondary=student_course, back_populates="courses")

engine = create_engine("sqlite:///student_system.db", echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

course_names = ["Math", "Physics", "History", "Programming", "Art"]
courses = [Course(name=name) for name in course_names]
session.add_all(courses)
session.commit()

for i in range(1, 21):
    student = Student(name=f"Student{i}")
    student.courses = random.sample(courses, k=random.randint(1, 3))
    session.add(student)
session.commit()

def add_student(name, course_ids):
    new_student = Student(name=name)
    new_student.courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
    session.add(new_student)
    session.commit()
    print(f"Student '{name}' added.")

def show_students_on_course(course_id):
    course = session.get(Course, course_id)
    if course:
        print(f"Students on course '{course.name}':")
        for s in course.students:
            print(f"- {s.name}")

def show_courses_of_student(student_id):
    student = session.get(Student, student_id)
    if student:
        print(f"Courses of student '{student.name}':")
        for c in student.courses:
            print(f"- {c.name}")

def update_student_name(student_id, new_name):
    student = session.get(Student, student_id)
    if student:
        student.name = new_name
        session.commit()
        print("Student name updated.")

def delete_student(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        print("Student deleted.")

add_student("NewStudent", [1, 3])
show_students_on_course(1)
show_courses_of_student(1)
update_student_name(1, "UpdatedStudent1")
delete_student(2)

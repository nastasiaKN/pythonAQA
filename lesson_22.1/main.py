from db_client import DBClient

if __name__ == '__main__':
    db = DBClient()

    db.seed_courses()
    db.seed_students()

    db.add_student("NewStudent", [1, 3])
    db.show_students_on_course(1)
    db.show_courses_of_student(1)
    db.update_student_name(1, "UpdatedStudent1")
    db.delete_student(2)
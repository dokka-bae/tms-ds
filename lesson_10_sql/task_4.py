from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from task_1 import Student, Course, StudentsCourses

engine = create_engine("sqlite:///db.db")
engine.connect()

Session = sessionmaker(autoflush=True, bind=engine)
session = Session()


def get_student_with_two_more_courses():
    subquery = select(StudentsCourses.student_id)\
        .group_by(StudentsCourses.student_id)\
        .having(func.count(StudentsCourses.student_id) > 2).scalar_subquery()

    query = select(Student)\
        .where(Student.id.in_(subquery))

    for student in session.execute(query).scalars().fetchall():
        print(student.id, student.name)


def get_courses_with_three_more_students():
    subquery = select(StudentsCourses.course_id)\
        .group_by(StudentsCourses.course_id)\
        .having(func.count(StudentsCourses.course_id) >= 3).scalar_subquery()

    query = select(Course).where(Course.id.in_(subquery))

    for course in session.execute(query).scalars().fetchall():
        print(course.id, course.name)


def get_students_of_course(course_name):
    subquery = select(Course.id).where(
        Course.name == course_name).scalar_subquery()

    query = select(Student)\
        .join(StudentsCourses, StudentsCourses.student_id == Student.id)\
        .where(StudentsCourses.course_id.in_(subquery))

    for student in session.execute(query).scalars().fetchall():
        print(student.id, student.name)


# get_student_with_two_more_courses()
# get_courses_with_three_more_students()
# get_students_of_course("Math")

# Задание: Напишите сложные запросы к базе данных
# 1. Получение списка студентов, у которых больше двух курсов
# 2. Получение списка курсов, на которые записано более трех студентов
# 3. Получение списка студентов, записанных на конкретный курс

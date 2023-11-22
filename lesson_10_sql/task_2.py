from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import task_1

# Создаем соединение к базе данных
engine = create_engine('sqlite:///db.db', echo=True)
engine.connect()

# Создаем сессию
Session = sessionmaker(autoflush=True, bind=engine)
session = Session()


def deleete_table(name):
    metadata = sqlalchemy.MetaData()
    metadata.reflect(bind=engine)
    metadata.tables.get("sqlite_master").drop(bind=engine)


def create_tables():
    task_1.Base.metadata.create_all(bind=engine)


def create_student(student_name):
    session.add(task_1.Student(name=student_name))
    session.commit()


def create_course(course_name):
    session.add(task_1.Course(name=course_name))
    session.commit()


def bind_student_on_course(student_id, course_id):
    session.add(task_1.StudentsCourses(
        student_id=student_id, course_id=course_id))
    session.commit()


def get_all_students():
    students = sqlalchemy.select(task_1.Student.id, task_1.Student.name)
    print(session.execute(students).fetchall())


def get_all_student_courses(student_id):
    courses_id = sqlalchemy.select(task_1.StudentsCourses.course_id).where(
        task_1.StudentsCourses.student_id == student_id)
    courses_id = session.execute(courses_id).fetchall()
    courses = []
    for id in courses_id:
        courses.append(sqlalchemy.select(
            task_1.Course.name).where(task_1.Course.id == id[0]))
    courses_name = []
    for name in courses:
        courses_name.append(session.execute(name).fetchall()[0][0])
    print(courses_name)


# create_tables()
# create_student(student_name="Vasiliy")
# create_course(course_name="Physics")
# bind_student_on_course(3,1)
# get_all_students()
# get_all_student_courses(1)

# Задание: Напишите запросы для следующих операций
# 1. Добавление студента в базу данных
# 2. Добавление курса в базу данных
# 3. Привязка студента к курсу
# 4. Получение списка всех студентов
# 5. Получение списка всех курсов для конкретного студента

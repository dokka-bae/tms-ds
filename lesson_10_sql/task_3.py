from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import task_1

engine = create_engine("sqlite:///db.db", echo=True)
engine.connect()

Session = sessionmaker(autoflush=True, bind=engine)
session = Session()


def rename_student(student_id, new_student_name):
    update_query = sqlalchemy.update(task_1.Student).where(
        task_1.Student.id == student_id).values(name=new_student_name)
    session.execute(update_query)
    session.commit()


def rename_course(course_id, new_course_name):
    update_query = sqlalchemy.update(task_1.Course).where(
        task_1.Course.id == course_id).values(name=new_course_name)
    session.execute(update_query)
    session.commit()


def delete_student(student_id):
    delete_query = sqlalchemy.delete(task_1.Student).where(
        task_1.Student.id == student_id)
    session.execute(delete_query)
    delete_query = sqlalchemy.delete(task_1.StudentsCourses).where(
        task_1.StudentsCourses.student_id == student_id)
    session.execute(delete_query)
    session.commit()


def delete_course(course_id):
    delete_query = sqlalchemy.delete(task_1.Course).where(
        task_1.Course.id == course_id)
    session.execute(delete_query)
    delete_query = sqlalchemy.delete(task_1.StudentsCourses).where(
        task_1.StudentsCourses.course_id == course_id)
    session.execute(delete_query)
    session.commit()


# rename_student(1,"Timofey")
# rename_course(1,"Math")
# delete_student(1)
# delete_course(2)


# Задание: Напишите код для обновления следующих данных
# 1. Изменение имени студента
# 2. Изменение названия курса
# 3. Удаление студента из базы данных
# 4. Удаление курса из базы данных

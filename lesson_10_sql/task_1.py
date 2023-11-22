from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class StudentsCourses(Base):
    __tablename__ = 'students_courses'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    course_id = Column(Integer)
    __table_args__ = (
        UniqueConstraint('student_id', 'course_id'),
    )

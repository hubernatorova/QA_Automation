from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,declarative_base
import random

Base = declarative_base()
student_course = Table('student_course', Base.metadata,
                       Column("student_id", Integer, ForeignKey('students.id'), primary_key=True),
                       Column("course_id", Integer, ForeignKey('courses.id'), primary_key=True),
                       )
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)

    courses = relationship("Course", secondary=student_course, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String,nullable=False)

    students = relationship("Student", secondary=student_course, back_populates="courses")

#Створення БД
engine = create_engine('sqlite:///students.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#Заповнення бази 5 курсами
courses = [Course(title=f"Курс{i}") for i in range(1,6)]
session.add_all(courses)
session.commit()

#Заповнення бази 20 студентами та рандомний розподіл їх по курсах
students = [Student(name=f"Студент{i}") for i in range(1, 21)]
session.add_all(students)
session.commit()

for student in students:
    student.courses = random.sample(courses, random.randint(1, 3))
session.commit()

#Функції для роботи з базою

def add_student(name):
    """Створює нового студента і додає його в базу"""
    student = Student(name=name)
    session.add(student)
    session.commit()
    print(f"Доданий студент: {name}")

def enroll_student(student_id, course_id):
    """Шукає студента і курс по id. Якщо знайдено, додає студента на курс"""
    student = session.get(Student,student_id)
    course = session.get(Course,course_id)
    if student and course:
        student.courses.append(course)
        session.commit()
        print(f"Студент{student.name} записаний на {course.title}")
    else:
        print("Студент або курс не знайдено")


def get_students_in_course(course_id):
    """Знаходить курс і повертає список студентів, записаних на нього"""
    course = session.get(Course, course_id)
    if course:
        return [student.name for student in course.students]
    return []

def get_courses_for_student(student_id):
    """Знаходить студента і повертає список його курсів"""
    student = session.get(Student, student_id)
    if student:
        return [course.title for course in student.courses]
    return []

def update_student(student_id, new_name):
    """Шукає студента і оновлює його імʼя"""
    student = session.get(Student, student_id)
    if student:
        student.name = new_name
        session.commit()
        print(f"Імʼя студента оновлено: {new_name}")
    else:
        print("Студента не знайдено")

def delete_student(student_id):
    """Видалення студента з бази"""
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Студент {student.name} видалений")
    else:
        print("Студента не знайдено")

# Приклад роботи з базою
add_student("Новий студент")
enroll_student(1, 3)
print("Студенти на курсі 3:", get_students_in_course(3))
print("Курси студента 1:", get_courses_for_student(1))
update_student(1, "Оновленне імʼя")
delete_student(2)

session.close()
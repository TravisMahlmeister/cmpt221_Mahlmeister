"""professor.py: create a table named professors in the marist database"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.server import Base

class Professor(Base):
    __tablename__ = 'Professors'

    # define primary key, autoincrement ensures no duplicates
    ProfessorID = Column(Integer, primary_key=True, autoincrement=True)

    # 40 = max length of string
    FirstName = Column(String(40))
    LastName = Column(String(40))
    Email = Column(String(100))

    # create many to many relationship with courses table through association/join table
    professor_courses = relationship("ProfessorCourse", back_populates="professor")
    courses = relationship("Course", secondary="ProfessorCourses", viewonly=True)

    def __repr__(self):
        return f"""FIRST NAME: {self.FirstName}, LAST NAME: {self.LastName}, EMAIL: {self.Email}
        """
    
"""course.py: create a table named courses in the marist database"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.server import Base

class Course(Base):
    __tablename__ = 'Courses'

    # define primary key, autoincrement ensures no duplicates
    CourseID = Column(Integer, primary_key=True, autoincrement=True)
    
    # 40 = max length of string
    CourseName = Column(String(40))
    Semester = Column(String(40))
    Year = Column(Integer)

    # create many to many relationship with professors table through association/join table
    professor_courses = relationship("ProfessorCourse", back_populates="course")
    professors = relationship("Professor", secondary="ProfessorCourses", viewonly=True)

    def __repr__(self):
        return f"""
            "COURSE NAME: {self.CourseName}, SEMESTER: {self.Semester}, YEAR: {self.Year}"""
    
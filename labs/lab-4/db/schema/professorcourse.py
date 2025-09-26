"""professorcourse.py: contains association tables for many to many relationships"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

# switched to a class (unlike in lab-3) to include additional relationship data
class ProfessorCourse(Base):
    __tablename__ = 'ProfessorCourses'
    
    # define primary key, autoincrement ensures no duplicates
    ProfessorCourseID = Column(Integer, primary_key=True, autoincrement=True)
    # define foreign keys
    ProfessorID = Column(Integer, ForeignKey('Professors.ProfessorID'), nullable=False)
    CourseID = Column(Integer, ForeignKey('Courses.CourseID'), nullable=False)
    
    # additional information
    Enrollment = Column(Integer)

    # since we have included additional information this time,
    # we are now using the association object pattern and need
    # to include this code
    professor = relationship("Professor", back_populates="professor_courses")
    course = relationship("Course", back_populates="professor_courses")
    
    def __repr__(self):
        return f"""
            "PROFESSOR ID: {self.ProfessorID}, COURSE ID: {self.CourseID}, ENROLLMENT: {self.Enrollment}
        """
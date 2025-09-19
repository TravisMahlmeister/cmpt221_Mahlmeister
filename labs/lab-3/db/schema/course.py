"""course.py: create a table named courses in the marist database"""
from db.server import db

class Course(db.Model):
    __tablename__ = 'Courses'
    # db.<data type> is the data type of the value in the column
    CourseID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    # 40 = max length of string
    CourseName = db.Column(db.String(40))
    Semester = db.Column(db.String(40))
    Year = db.Column(db.Integer)

    # create relationship with professors table. assoc table name = ProfessorCourse
    Professor = db.relationship('Professors', secondary = 'ProfessorCourse', back_populates = 'Courses')
    def __init__(self, name):
        self.CourseName = self.CourseName
        self.Semester = self.Semester
        self.Year = self.Year

    def __repr__(self):
        return f"""
            "COURSE NAME: {self.CourseName},
             SEMESTER: {self.Semester},
             YEAR: {self.Year}
        """
    
    def __repr__(self):
        return self.__repr__()
    
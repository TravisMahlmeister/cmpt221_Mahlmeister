"""professorcourse.py: contains association tables for many to many relationships"""
from db.server import db

# join table between professors and courses
ProfessorCourse = db.Table(
  'ProfessorCourse',
  # grab the professor primary key and make it a foreign key
  db.Column('ProfessorID', db.Integer, db.ForeignKey('Professors.ProfessorID')),
  # grab the course primary key and make it a foreign key
  db.Column('CourseID', db.Integer, db.ForeignKey('Courses.CourseID'))
)
# import all tables (models) so they get registered with Base.metadata
from .course import Course
from .professor import Professor
from .professorcourse import ProfessorCourse

# make tables (models) available when importing from schema package
__all__ = ['Course', 'Professor', 'ProfessorCourse']
"""orm.py: sqlalchemy orm used to manage the Professors table"""
from db.server import get_session
from db.schema import Professor

"""Lab 4 - Part 2:
- Insert 3 records into the Professors table
- Update 1 record in the Professors table
- Delete 1 record in the Professors table
"""

def get_all_professors():
    """Select all records from the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # get all entries in the Professors table
        professors = session.query(Professor).all()
        return professors
    
    finally:
        session.close()

def insert_professors():
    """Insert 3 records into the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # TODO: create three professor objects
        professor1 = Professor(FirstName="Alex", LastName="Mahlmeister", Email="Alex.Mahlmeister1@marist.edu")
        professor2 = Professor(FirstName="Cooper", LastName="Mahlmeister", Email="Cooper.Mahlmeister1@marist.edu")
        professor3 = Professor(FirstName="Ryan", LastName="Mahlmeister", Email="Ryan.Mahlmeister1@marist.edu")
        # TODO: use the sqlalchemy orm to insert the new records as a list of professor objects
        session.add_all([professor1, professor2, professor3])
        # "save" the changes
        session.commit()

    except Exception as e:
        session.rollback()
        print("Error inserting professors:", e)

    finally:
        session.close()

def update_professor():
    """Update one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # TODO: get professor to be updated (would ideally be a parameter)
        professor = session.query(Professor).filter(Professor.ProfessorID == 2).one_or_none()
        # TODO: use the sqlalchemy orm to update 1 record
        if professor:
            professor.FirstName = "Cali"
            # "save" the changes
            session.commit()
        else:
            print(f"No professor found with that ID")
    
    except Exception as e:
        session.rollback()
        print("Error updating professor:", e)
        
    finally:
        session.close()

def delete_professor():
    """Delete one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # TODO: get professor to be deleted (would ideally be a parameter)
        professor = session.query(Professor).filter(Professor.ProfessorID == 3).one_or_none()

        if professor:
            session.delete(professor)
            # TODO: use the sqlalchemy orm to delete 1 record
            # "save" the changes
            session.commit()
        else:
            print(f"No professor foudn with that ID")

    except Exception as e:
        session.rollback()
        print("Error updating professor:", e)

    finally:
        session.close()


"""sql.py: queries used to manage the Courses table"""
from sqlalchemy import text
from db.server import get_session

"""Lab 4 - Part 1:
- Insert 3 records into the Courses table
- Update 1 record in the Courses table
- Delete 1 record in the Courses table
"""

def get_all_courses():
    """Select all records from the Courses table using SQL."""
    session = get_session()
    try:
        query = """
        SELECT * FROM "Courses";
        """
        # fetchall() retrieves all rows from a query and returns them as a list
        result = session.execute(text(query)).fetchall()
        return result
    
    finally:
        session.close()

def insert_courses():
    """Insert 3 records into the Courses table using SQL."""
    session = get_session()
    try:
        # TODO: write a SQL query to insert 3 records 
        query = """
        """
        session.execute(text(query))
        session.commit()

    except Exception as e:
        session.rollback()
        print("Error inserting courses:", e)

    finally:
        session.close()

def update_course():
    """Update one record in the Courses table using SQL."""
    session = get_session()
    try:
        # TODO: write a SQL query to update 1 record
        query = """
        """
        result = session.execute(text(query))
        # "save" the changes
        session.commit()
        return result
    
    except Exception as e:
        session.rollback()
        print("Error updating course:", e)

    finally:
        session.close()

def delete_course():
    """Delete one record in the Courses table using SQL."""
    session = get_session()
    try:
        # TODO: write a SQL query to delete 1 record
        query = """
        """
        result = session.execute(text(query))
        # "save" the changes
        session.commit()
        return result
    
    except Exception as e:
        session.rollback()
        print("Error deleting course:", e)

    finally:
        session.close()
"""query.py: leverages SQLAlchemy to create generic queries for interacting with the postgres DB"""
from db.server import get_session

def get_all(table) -> list:
    """Select all records from a DB table using SQLAlchemy ORM.

        args: 
            table (object): db table

        returns:
            records (list[obj]): list of records from db table
    """
    session = get_session()
    try:
        # get all records in the table
        records = session.query(table).all()
        return records
    
    finally:
        session.close()

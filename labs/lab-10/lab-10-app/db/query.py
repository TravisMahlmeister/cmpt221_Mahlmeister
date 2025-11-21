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

def get_one(table, **filters) -> object:
    """Select one record from a DB table using SQLAlchemy ORM.

        args: 
            table (object): db table
            **filters: the attribute(s) to query by

        returns:
            record (object): one record from the db table
    """
    session = get_session()
    try:
        # get one record from the table
        record = session.query(table).filter_by(**filters).first()
        return record
    
    finally:
        session.close()


def insert(record) -> None:
    """Insert one record into a table
    
        args: 
            record (object): record to insert into db

        returns:
            none
    """
    session = get_session()

    try:
        # insert one new record
        session.add(record)
        # "save" the changes
        session.commit()

    except Exception as e:
        session.rollback()
        print("Error inserting records:", e)

    finally:
        session.close()



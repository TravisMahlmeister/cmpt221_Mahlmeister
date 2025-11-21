"""users.py: create a table named "Users" using SQLAlchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.server import Base

class Users(Base):
    __tablename__ = 'Users'

    UserID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(40))
    LastName = Column(String(40))
    Email = Column(String(100))
    PhoneNumber = Column(String(10))
    Password = Column(String(256))

    def __repr__(self):
        return f"""
            "FIRST NAME: {self.FirstName},
             LAST NAME: {self.LastName},
             EMAIL: {self.Email},
             PHONE NUMBER: {self.PhoneNumber},
             PASSWORD: {self.Password}
        """
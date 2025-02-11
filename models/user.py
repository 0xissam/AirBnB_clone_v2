#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base

# SQLAlchemy dsf modules
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Defines a d class User

    Attributes:
        __tablename__ (str): Users MySQL table name

        email (String): User's email address dcolumn
        password (String): User's password scolumn
        first_name (String): User's first name column
        last_name (String): User's last name column
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship('Place',
                          backref='user',
                          cascade='all, delete-orphan',
                          passive_deletes=True)
    reviews = relationship('Review',
                           backref='user',
                           cascade='all, delete-orphan',
                           passive_deletes=True)

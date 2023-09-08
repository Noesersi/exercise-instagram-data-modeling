import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False)


class Follower(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('Users.id'))
    user_to_id = Column(Integer, nullable=False)

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))


class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.id'))

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    Comment_text = Column(String)
    author_id = Column(Integer, ForeignKey('Users.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

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
    posts = relationship('Post', backref='user')
    comments = relationship('Comment', backref='author')
    # aqui me he liado un poco con los nombres, no estoy seguro de quien sigue a quien
    following = relationship('Follower', foreign_keys=('Follower.user_from_id'), backref='follower')
    followers = relationship('Follower', foreign_keys=('Follower.user_to_id'), backref='user')

class Follower(Base):
    __tablename__ = 'Follower'
    id= Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('Users.id'))
    user_to_id = Column(Integer, nullable=False)
    followed = relationship('Users', foreign_keys=('user_from_id'), backref='followers')
    follower = relationship('Users', foreign_keys=('user_to_id'), backref='following')

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship('Users', backref='posts')
    media = relationship('Media', backref='post')
    comments = relationship('Comment', backref='post')


class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.id'))
    post = relationship('Post', backref='media')

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    Comment_text = Column(String)
    author_id = Column(Integer, ForeignKey('Users.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))
    author = relationship('Users', backref='comments')
    post = relationship('Post', backref='comments')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

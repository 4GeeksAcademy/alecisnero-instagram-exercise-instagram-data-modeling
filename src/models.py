import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True, nullable=False)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False) 
    usarname = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True,nullable=False)
    post_id = Column(Integer, ForeignKey('user.id'),nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id =Column(Integer, primary_key=True, nullable=False) 
    type =Column(String(250), nullable=True)
    url =Column(String(250), nullable=False) 
    post_id =Column(Integer, ForeignKey('post.id'), nullable=False)

class Commets(Base):
    __tablename__ = 'commets'
    id = Column(Integer, primary_key=True, nullable=False)
    author_id = Column(String(250), ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    text = Column(Integer, nullable=False)



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

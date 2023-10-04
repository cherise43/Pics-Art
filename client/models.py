from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import DateTime,func
db=SQLAlchemy()
class User(db.Model,SerializerMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String)
    password=db.Column(db.String)
    pics=db.relationship('Pic',backref='user')

class Pic(db.Model,SerializerMixin):
    __tablename__='pics'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer)
    caption=db.Column(db.String)
    image_url=db.Column(db.String)
    created_at = db.Column(DateTime, default=func.current_timestamp())
    users=db.relationship('User',back_populates='pics')

class Sketch(db.Model,SerializerMixin):
    __tablename__='sketchs'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    description=db.Column(db.String)
    image_url=db.Column(db.String)
    created_at = db.Column(DateTime, default=func.current_timestamp())
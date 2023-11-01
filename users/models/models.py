from users.connections.connectors import app, db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title})"


with app.app_context():
    db.create_all()
    # db.drop_all()




# from owsresponse import response
# from sqlalchemy import Boolean
# from sqlalchemy import case
# from sqlalchemy import Column
# from sqlalchemy import DATETIME
# from sqlalchemy import Enum
# from sqlalchemy import ForeignKey
# from sqlalchemy import func
# from sqlalchemy import Integer
# from sqlalchemy import String
# from sqlalchemy.orm import relationship
#
# from users import constants as const
# from users.connectors import mysql
# from users.models.sql import document
#
#
# class OAUser(mysql.BaseModel):
#     """OA User Model."""
#
#     __tablename__ = 'orchadmin_users'
#
#     user_id = Column(Integer, name='id', primary_key=True, nullable=False)
#     first_name = Column(String, name='f_name', nullable=False)
#     last_name = Column(String, name='l_name', nullable=False)
#     email = Column(String, name='email')
#     active = Column(String, name='active')
#     auth0_user_id = Column(String)
#     office_phone = Column(String, name='office_phone')
#     is_product_manager = Column(Boolean, name='is_product_manager')

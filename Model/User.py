from sqlalchemy import Column, INTEGER, VARCHAR, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base


DataBase = declarative_base()


class User(DataBase):
    __tablename__ = 'user'

    id = Column('id', INTEGER, autoincrement=True)
    name = Column('name', VARCHAR(30), nullable=True)
    surname = Column('surname', VARCHAR(30), nullable=True)
    mail = Column('mail', VARCHAR(13), nullable=False)
    login = Column('login', VARCHAR(50), nullable=False)
    password = Column('password', VARCHAR(50), nullable=False)

    PrimaryKeyConstraint(id, name='PK_User_Id')
    UniqueConstraint(mail, name='UQ_User_mail')

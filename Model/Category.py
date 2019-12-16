from sqlalchemy import Column, INTEGER, VARCHAR, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


DataBase = declarative_base()


class Category(DataBase):
    __tablename__ = "category"

    id = Column('id', INTEGER, autoincrement=True)
    title = Column('title', VARCHAR(1000), nullable=False)
    user_id = Column('user_id', INTEGER, ForeignKey("user.id"), nullable=False)

    PrimaryKeyConstraint(id, name="PK_Category_Id")
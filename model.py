from sqlalchemy import create_engine,Integer,String,Table,ForeignKey,Column,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker

engine = create_engine('sqlite:///database.db',echo=True)

Base = declarative_base()

class User(Base): 
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True,nullable=False)
    full_name= Column(String,nullable=False)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)

    
class Orders(Base): 
    __tablename__= 'orders'
    id = Column(Integer,primary_key=True)
    order_date = Column(String,nullable=False)
    status = Column(String,nullable=False)
    order_total = Column(Float, nullable=False)


class Items(Base): 
    __tablename__= 'items'
    id = Column(Integer,primary_key=True)
    tracking_number = Column(String,nullable=False)
    status = Column(String,nullable=False)
    country= Column(String,nullable=False)
    receiving_date = Column(String,nullable=False)
    item_weight = Column(Integer)
    item_price = Column(Float)
    quantity = Column(Integer)
    user = Column(Integer,nullable=False)




Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


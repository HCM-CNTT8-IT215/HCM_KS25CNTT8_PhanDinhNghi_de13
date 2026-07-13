from sqlalchemy import Column, String, Integer

from database import Base

class Patients(Base):
    __tablename__="patients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    address = Column(String,nullable=False)
    insurance_type = Column(String,nullable=False)
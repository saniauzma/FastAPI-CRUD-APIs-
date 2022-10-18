from database import Base
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship


class Employees(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key = True)
    emp_name = Column(String(255), unique=True)
    Org_id = Column(Integer, ForeignKey("orgnaizations.Org_id"))

    Org = relationship("Organizations", back_populates="Emp")

    # def __repr__(self):
    #     return f"<emp_id={self.id} emp_name={self.emp_name} org_id={self.Org_id}"


class Organizations(Base):
    __tablename__ = "orgnaizations"
    Org_id = Column(Integer, primary_key = True)
    Org_name = Column(String)

    Emp = relationship("Employees", back_populates="Org")



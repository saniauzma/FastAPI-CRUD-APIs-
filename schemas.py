from pydantic import BaseModel
from typing import List, Optional


class OrganizationsAll(BaseModel):
    Org_id:int
    Org_name : str

    class Config:
        orm_mode = True



class EmployeesAll(BaseModel):
    emp_name : str
    Org_id : int 

    class Config:
        orm_mode = True



class EmployeeWithOrg(BaseModel):
    id:int
    emp_name: str
    Org : OrganizationsAll

    class Config:
        orm_mode = True


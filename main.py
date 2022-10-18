from fastapi import FastAPI, HTTPException, status
from database import sessionLocal
from fastapi_sql.models import Employees
import models
from schemas import EmployeesAll, OrganizationsAll, EmployeeWithOrg
from typing import List

app = FastAPI()
db = sessionLocal()

# get all employees


@app.get('/employees', response_model=List[EmployeeWithOrg], status_code=200, tags=['Employees'])
def get_all_employees():
    employees = db.query(models.Employees).all()
    return employees

# get employee by id


@app.get('/employee/{id}', response_model=EmployeeWithOrg, status_code=status.HTTP_200_OK, tags=['Employees'])
def get_an_employee(id: int):
    emp = db.query(models.Employees).filter(models.Employees.id == id).first()
    return emp


# create an employee
@app.post('/employee', response_model=EmployeesAll, status_code=status.HTTP_201_CREATED, tags=['Employees'])
def create_an_employee(employee: EmployeesAll):
    new_emp = models.Employees(
        emp_name=employee.emp_name, Org_id=employee.Org_id)

    db.add(new_emp)
    db.commit()
    return new_emp

# update an employee


@app.put('/employee/{id}', response_model=EmployeesAll, status_code=status.HTTP_200_OK, tags=['Employees'])
def update_an_employee(id: int, employee: EmployeesAll):
    emp_to_update = db.query(models.Employees).filter(
        models.Employees.id == id).first()
    emp_to_update.emp_name = employee.emp_name
    emp_to_update.Org_id = employee.Org_id

    db.commit()
    return emp_to_update

# delete an employee


@app.delete('/employee/{id}', tags=['Employees'])
def delete_an_employee(id: int):
    emp_to_delete = db.query(models.Employees).filter(
        models.Employees.id == id).first()

    if emp_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")

    db.delete(emp_to_delete)
    db.commit()
    return emp_to_delete

# get employee of organization by Org_id


@app.get('/employeesOfOrg/{Org_id}', tags=['Employees and Organization'])
def get_emp_of_org(Org_id: int):
    emp = db.query(models.Employees.id, models.Employees.emp_name, models.Organizations.Org_id, models.Organizations.Org_name).join(models.Organizations,
                                                                                                                                    models.Employees.Org_id == models.Organizations.Org_id).filter(models.Employees.Org_id == Org_id).all()
    return emp

# create an organization


@app.post('/organization/', response_model=OrganizationsAll, status_code=status.HTTP_201_CREATED, tags=['Organizations'])
def create_org(organization: OrganizationsAll):
    db_Org = db.query(models.Organizations).filter(
        models.Organizations.Org_name == organization.Org_name).first()

    if db_Org:
        raise HTTPException(
            status_code=400, detail="Organization already exists")

    new_Org = models.Organizations(
        Org_id=organization.Org_id,
        Org_name=organization.Org_name
    )
    db.add(new_Org)
    db.commit()
    return new_Org

# get all organizations


@app.get('/organizations', response_model=List[OrganizationsAll], status_code=200, tags=['Organizations'])
def get_Organizations():
    Orgs = db.query(models.Organizations).all()
    return Orgs

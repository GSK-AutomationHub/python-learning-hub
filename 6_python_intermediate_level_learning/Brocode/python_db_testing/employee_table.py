
import sqlite3
from employee_info import Employee

connect = sqlite3.connect(':memory:')
cursor = connect.cursor()

def create_employee_table():
    cursor.execute("CREATE TABLE EMPLOYEE (name TEXT, role TEXT, salary INTEGER )")
    connect.commit()


def insert_employee_record(emp):
    with connect:
        cursor.execute("INSERT INTO EMPLOYEE VALUES (:name, :role, :salary)",
                    {'name' : emp.name, 'role': emp.role, 'salary': emp.salary})


def get_employee_record(emp):
    with connect:
        cursor.execute("SELECT * FROM EMPLOYEE WHERE name = :name",
                    {'name' : emp.name})
        return cursor.fetchone()


def update_employee_record(emp, sal_value):
    with connect:
        cursor.execute("UPDATE EMPLOYEE SET salary = :salary WHERE name = :name",
                    {'salary' : sal_value, 'name' : emp.name})

    

def delete_employee_record(emp):
    with connect:
        cursor.execute("DELETE * FROM EMPLOYEE WHERE name = :name",
                    {'name' : emp.name})
    

emp = Employee.create_employee()

create_employee_table()

insert_employee_record(emp)

print(get_employee_record(emp))

update_employee_record(emp, 600000)

print(get_employee_record(emp))

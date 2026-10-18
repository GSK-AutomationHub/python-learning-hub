
class Employee:

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary


    def __str__(self):
        return f"Name: {self.name}, Profile: {self.role}, Compensation: {self.salary}"
    

    @staticmethod
    def create_employee():
        emp0 = Employee('Advait', 'CTO', 500000)
        return emp0


    @staticmethod
    def create_employees():
        emp1 = Employee('Akash', 'Architect', 150000)
        emp2 = Employee('Aman', 'Project Mngr', 120000)
        emp3 = Employee('Abhay', 'Dev Lead', 100000)
        return [emp1, emp2, emp3]


# emp = Employee('Lokesh', 'QA Lead', '2500000')
# print(emp)
"""
I didn't need to use ChatGPT to make Employee.py
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def update_salary(self):
        return self.salary * 1.1

a = Employee("John", 5000)
print(a.update_salary())
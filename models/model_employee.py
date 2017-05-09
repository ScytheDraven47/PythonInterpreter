# Ben Rogers-McKee (ScytheDraven47)
# 09/05/2017
#
# Validation file for Interpreter project

from models.model_validator import Validate


class Employee:
    def __init__(self, employee_data):
        self.emp_id = employee_data['emp_id']
        self.gender = employee_data['gender']
        self.age = employee_data['age']
        self.sales = employee_data['sales']
        self.bmi = employee_data['bmi']
        self.salary = employee_data['salary']
        self.birthday = employee_data['birthday']

    def validate_employee(self):
        v = Validate()
        checklist = {'emp_id': v.validate_emp_id(self.emp_id),
                     'gender': v.validate_gender(self.gender),
                     'age': v.validate_age(self.age),
                     'sales': v.validate_sales(self.sales),
                     'bmi': v.validate_emp_id(self.bmi),
                     'salary': v.validate_salary(self.salary),
                     'birthday': v.validate_birthday(self.birthday)}
        return checklist

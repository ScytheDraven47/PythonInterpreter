# Ben Rogers-McKee (ScytheDraven47)
# 25/03/2017
#
# Unit testing for Validate model of Interpreter project

import unittest
from datetime import datetime
from models.model_validator import Validate

v = Validate()


class TestValidate(unittest.TestCase):
    def test_validate_emp_id_true(self):
        self.assertEqual(v.validate_emp_id("A001"), True)
        self.assertEqual(v.validate_emp_id("Z999"), True)

    def test_validate_emp_id_false(self):
        self.assertEqual(v.validate_emp_id("a001"), False)
        self.assertEqual(v.validate_emp_id("A01"), False)
        self.assertEqual(v.validate_emp_id(999), False)
        self.assertEqual(v.validate_emp_id(None), False)

    def test_validate_gender_true(self):
        self.assertEqual(v.validate_gender("M"), True)
        self.assertEqual(v.validate_gender("f"), True)

    def test_validate_gender_false(self):
        self.assertEqual(v.validate_gender("Male"), False)
        self.assertEqual(v.validate_gender("girl"), False)
        self.assertEqual(v.validate_gender(None), False)

    def test_validate_age_true(self):
        self.assertEqual(v.validate_age("22"), True)
        self.assertEqual(v.validate_age(22), True)

    def test_validate_age_false(self):
        self.assertEqual(v.validate_age("100"), False)
        self.assertEqual(v.validate_age(-1), False)
        self.assertEqual(v.validate_age(""), False)

    def test_validate_sales_true(self):
        self.assertEqual(v.validate_sales("18"), True)
        self.assertEqual(v.validate_sales(783), True)

    def test_validate_sales_false(self):
        self.assertEqual(v.validate_sales(-1), False)
        self.assertEqual(v.validate_sales("1000"), False)
        self.assertEqual(v.validate_sales(""), False)

    def test_validate_bmi_true(self):
        self.assertEqual(v.validate_bmi("Normal"), True)
        self.assertEqual(v.validate_bmi("underweight"), True)

    def test_validate_bmi_false(self):
        self.assertEqual(v.validate_bmi("skinny"), False)
        self.assertEqual(v.validate_bmi(60), False)
        self.assertEqual(v.validate_bmi(""), False)

    def test_validate_salary_true(self):
        self.assertEqual(v.validate_salary("999"), True)
        self.assertEqual(v.validate_salary(10), True)

    def test_validate_salary_false(self):
        self.assertEqual(v.validate_salary(180000), False)
        self.assertEqual(v.validate_salary("999,999"), False)
        self.assertEqual(v.validate_salary("Lots"), False)
        self.assertEqual(v.validate_salary(""), False)

    def test_validate_birthday_true(self):
        self.assertEqual(v.validate_birthday("08-07-1994"), True)
        self.assertEqual(v.validate_birthday(datetime.now()), True)

    def test_validate_birthday_false(self):
        self.assertEqual(v.validate_birthday("1994-07-08"), False)
        self.assertEqual(v.validate_birthday("30-02-2017"), False)
        self.assertEqual(v.validate_birthday(""), False)

    def test_validate_age_birthday_true(self):
        self.assertEqual(v.validate_age_birthday("22", "08-07-1994"), True)
        self.assertEqual(v.validate_age_birthday(16, datetime.strptime("03-10-2000", "%d-%m-%Y")), True)

    def test_validate_age_birthday_false(self):
        self.assertEqual(v.validate_age_birthday("16", datetime.strptime("03-10-1994", "%d-%m-%Y")), False)
        self.assertEqual(v.validate_age_birthday(42, "08-07-1994"), False)
        self.assertEqual(v.validate_age_birthday(22, "24-03-1994"), False)

    def test_validate_all_true(self):
        self.assertEqual(
            v.validate_all(
                {"emp_id": "A001",
                 "gender": "M",
                 "age": 22,
                 "sales": 42,
                 "bmi": "Normal",
                 "salary": 180,
                 "birthday": datetime.strptime("08-07-1994", "%d-%m-%Y")}),
                {"emp_id": True,
                 "gender": True,
                 "age": True,
                 "sales": True,
                 "bmi": True,
                 "salary": True,
                 "birthday": True})
        self.assertEqual(
            v.validate_all(
                {"emp_id": "Z999",
                 "gender": "f",
                 "age": "22",
                 "sales": "42",
                 "bmi": "normal",
                 "salary": "180",
                 "birthday": "08-07-1994"}),
                {"emp_id": True,
                 "gender": True,
                 "age": True,
                 "sales": True,
                 "bmi": True,
                 "salary": True,
                 "birthday": True})

    def test_validate_all_false(self):
        self.assertEqual(
            v.validate_all(
                {"emp_id": "a001",
                 "gender": "M",
                 "age": 22,
                 "sales": 42,
                 "bmi": "Normal",
                 "salary": 180,
                 "birthday": datetime.strptime("08-07-1994", "%d-%m-%Y")}),
                {"emp_id": False,
                 "gender": True,
                 "age": True,
                 "sales": True,
                 "bmi": True,
                 "salary": True,
                 "birthday": True})
        self.assertEqual(
            v.validate_all(
                {"emp_id": "a001",
                 "gender": "Male",
                 "age": 22,
                 "sales": 42,
                 "bmi": "Normal",
                 "salary": 180,
                 "birthday": datetime.strptime("08-07-1994", "%d-%m-%Y")}),
                {"emp_id": False,
                 "gender": False,
                 "age": True,
                 "sales": True,
                 "bmi": True,
                 "salary": True,
                 "birthday": True})
        self.assertEqual(
            v.validate_all(
                {"emp_id": "a001",
                 "gender": "Male",
                 "age": -1,
                 "sales": 42,
                 "bmi": "Normal",
                 "salary": 180,
                 "birthday": datetime.strptime("08-07-1994", "%d-%m-%Y")}),
                {"emp_id": False,
                 "gender": False,
                 "age": False,
                 "sales": True,
                 "bmi": True,
                 "salary": True,
                 "birthday": True})
        self.assertEqual(
            v.validate_all(
                {"emp_id": "a001",
                 "gender": "Male",
                 "age": -1,
                 "sales": 9999,
                 "bmi": "Normal",
                 "salary": 180,
                 "birthday": datetime.strptime("08-07-1994", "%d-%m-%Y")}),
                {"emp_id": False,
                 "gender": False,
                 "age": False,
                 "sales": False,
                 "bmi": True,
                 "salary": True,
                 "birthday": True})
        self.assertEqual(
            v.validate_all(
                {"emp_id": "a001",
                 "gender": "Male",
                 "age": -1,
                 "sales": 9999,
                 "bmi": "skinny",
                 "salary": 180,
                 "birthday": datetime.strptime("08-07-1994", "%d-%m-%Y")}),
                {"emp_id": False,
                 "gender": False,
                 "age": False,
                 "sales": False,
                 "bmi": False,
                 "salary": True,
                 "birthday": True})
        self.assertEqual(
            v.validate_all(
                {"emp_id": "a001",
                 "gender": "Male",
                 "age": -1,
                 "sales": 9999,
                 "bmi": "skinny",
                 "salary": "Lots",
                 "birthday": datetime.strptime("08-07-1994", "%d-%m-%Y")}),
                {"emp_id": False,
                 "gender": False,
                 "age": False,
                 "sales": False,
                 "bmi": False,
                 "salary": False,
                 "birthday": True})
        self.assertEqual(
            v.validate_all(
                {"emp_id": "a001",
                 "gender": "Male",
                 "age": -1,
                 "sales": 9999,
                 "bmi": "skinny",
                 "salary": "Lots",
                 "birthday": "61-12-1923"}),
                {"emp_id": False,
                 "gender": False,
                 "age": False,
                 "sales": False,
                 "bmi": False,
                 "salary": False,
                 "birthday": False})

if __name__ == '__main__':
    unittest.main()

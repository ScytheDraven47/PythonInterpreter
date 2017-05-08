# Ben Rogers-McKee (ScytheDraven47)
# 04/05/2017
#
# Unit testing for PythonInterpreter project

import unittest
from datetime import datetime
from unittest.mock import patch
from views.database_view import DatabaseView
from models.model_validator import Validate
from main import MainFlow
from views.console_view import ConsoleView
from views.excel_view import ExcelView


class TestPythonInterpreter(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseView()
        self.v = Validate()
        self.mf = MainFlow()
        self.c = ConsoleView()
        self.ex = ExcelView()

    # Test model_validator
    def test_validate_emp_id_true(self):
        self.assertEqual(self.v.validate_emp_id("A001"), True)
        self.assertEqual(self.v.validate_emp_id("Z999"), True)

    def test_validate_emp_id_false(self):
        self.assertEqual(self.v.validate_emp_id("a001"), False)
        self.assertEqual(self.v.validate_emp_id("A01"), False)
        self.assertEqual(self.v.validate_emp_id(999), False)
        self.assertEqual(self.v.validate_emp_id(None), False)

    def test_validate_gender_true(self):
        self.assertEqual(self.v.validate_gender("M"), True)
        self.assertEqual(self.v.validate_gender("f"), True)

    def test_validate_gender_false(self):
        self.assertEqual(self.v.validate_gender("Male"), False)
        self.assertEqual(self.v.validate_gender("girl"), False)
        self.assertEqual(self.v.validate_gender(None), False)

    def test_validate_age_true(self):
        self.assertEqual(self.v.validate_age("22"), True)
        self.assertEqual(self.v.validate_age(22), True)

    def test_validate_age_false(self):
        self.assertEqual(self.v.validate_age("100"), False)
        self.assertEqual(self.v.validate_age(-1), False)
        self.assertEqual(self.v.validate_age(""), False)

    def test_validate_sales_true(self):
        self.assertEqual(self.v.validate_sales("18"), True)
        self.assertEqual(self.v.validate_sales(783), True)

    def test_validate_sales_false(self):
        self.assertEqual(self.v.validate_sales(-1), False)
        self.assertEqual(self.v.validate_sales("1000"), False)
        self.assertEqual(self.v.validate_sales(""), False)

    def test_validate_bmi_true(self):
        self.assertEqual(self.v.validate_bmi("Normal"), True)
        self.assertEqual(self.v.validate_bmi("underweight"), True)

    def test_validate_bmi_false(self):
        self.assertEqual(self.v.validate_bmi("skinny"), False)
        self.assertEqual(self.v.validate_bmi(60), False)
        self.assertEqual(self.v.validate_bmi(""), False)

    def test_validate_salary_true(self):
        self.assertEqual(self.v.validate_salary("999"), True)
        self.assertEqual(self.v.validate_salary(10), True)

    def test_validate_salary_false(self):
        self.assertEqual(self.v.validate_salary(180000), False)
        self.assertEqual(self.v.validate_salary("999,999"), False)
        self.assertEqual(self.v.validate_salary("Lots"), False)
        self.assertEqual(self.v.validate_salary(""), False)

    def test_validate_birthday_true(self):
        self.assertEqual(self.v.validate_birthday("08-07-1994"), True)
        self.assertEqual(self.v.validate_birthday(datetime.now()), True)

    def test_validate_birthday_false(self):
        self.assertEqual(self.v.validate_birthday("1994-07-08"), False)
        self.assertEqual(self.v.validate_birthday("30-02-2017"), False)
        self.assertEqual(self.v.validate_birthday(8071994), False)
        self.assertEqual(self.v.validate_birthday(""), False)

    def test_validate_age_birthday_true(self):
        self.assertEqual(self.v.validate_age_birthday("22", "08-07-1994"), True)
        self.assertEqual(self.v.validate_age_birthday(16, datetime.strptime("03-10-2000", "%d-%m-%Y")), True)

    def test_validate_age_birthday_false(self):
        self.assertEqual(self.v.validate_age_birthday("16", datetime.strptime("03-10-1994", "%d-%m-%Y")), False)
        self.assertEqual(self.v.validate_age_birthday(42, "08-07-1994"), False)
        self.assertEqual(self.v.validate_age_birthday(22, "24-03-1994"), False)

    def test_validate_all_true(self):
        self.assertEqual(
            self.v.validate_all(
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
            self.v.validate_all(
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
            self.v.validate_all(
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
            self.v.validate_all(
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
            self.v.validate_all(
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
            self.v.validate_all(
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
            self.v.validate_all(
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
            self.v.validate_all(
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
            self.v.validate_all(
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

    # Test database_view
    def test_database_output_new_file(self):
        example_data = [{
            'emp_id': 'A001',
            'gender': 'M',
            'age': 42,
            'sales': 666,
            'bmi': 'Normal',
            'salary': 180,
            'birthday': '08-07-1994',
        }]
        filename = "data_src/db_test_001.db"
        from os import remove
        try:
            remove(filename)
        except OSError:
            pass
        self.db.output(example_data, filename)
        self.assertEqual(self.db.has_connected_to_db, True)
        self.assertEqual(self.db.has_created_db_if_did_not_exist, True)
        self.assertEqual(self.db.has_selected_data_from_db, False)
        self.assertEqual(self.db.has_filled_db, True)
        self.assertEqual(self.db.has_closed_db, True)
        remove(filename)

    def test_database_output_existing_file(self):
        example_data = [{
            'emp_id': 'A001',
            'gender': 'M',
            'age': 42,
            'sales': 666,
            'bmi': 'Normal',
            'salary': 180,
            'birthday': '08-07-1994',
        }]
        filename = "data_src/db_test_001.db"
        from os import remove
        try:
            remove(filename)
        except OSError:
            pass
        self.db.output([], filename)
        self.db.output(example_data, filename)
        self.assertEqual(self.db.has_connected_to_db, True)
        self.assertEqual(self.db.has_created_db_if_did_not_exist, True)
        self.assertEqual(self.db.has_selected_data_from_db, False)
        self.assertEqual(self.db.has_filled_db, True)
        self.assertEqual(self.db.has_closed_db, True)
        remove(filename)

    def test_database_output_bad_data(self):
        example_data = [{
            'emp_id': 'A001',
            'gender': 'M',
            'age': 42,
            'sales': 666,
            'bmi': 'Normal',
            'salary': 180,
            'birthday': '08-07-1994',
        }]
        filename = "data_src/db_test_001.db"
        from os import remove
        try:
            remove(filename)
        except OSError:
            pass
        self.db.output(example_data, filename)
        db2 = DatabaseView()
        db2.output(example_data, filename)
        self.assertEqual(db2.has_connected_to_db, True)
        self.assertEqual(db2.has_created_db_if_did_not_exist, True)
        self.assertEqual(db2.has_selected_data_from_db, False)
        self.assertEqual(db2.has_filled_db, False)
        self.assertEqual(db2.has_closed_db, True)
        remove(filename)

    def test_database_get_data(self):
        example_data = [{
            'emp_id': 'A001',
            'gender': 'M',
            'age': 42,
            'sales': 666,
            'bmi': 'Normal',
            'salary': 180,
            'birthday': '08-07-1994',
        }]
        filename = "data_src/db_test_001.db"
        self.db.output(example_data, filename)
        db2 = DatabaseView()
        db2.get_data(filename)
        self.assertEqual(db2.has_connected_to_db, True)
        self.assertEqual(db2.has_created_db_if_did_not_exist, False)
        self.assertEqual(db2.has_selected_data_from_db, True)
        self.assertEqual(db2.has_filled_db, False)
        self.assertEqual(db2.has_closed_db, True)
        from os import remove
        remove(filename)

    # Test main
    def test_main_do_show_data_without_flag(self):
        expected = 0
        actual = self.mf.do_show_data("")
        self.assertEqual(expected, actual)

    def test_main_do_show_data_with_flag(self):
        expected = 1
        actual = self.mf.do_show_data("-f")
        self.assertEqual(expected, actual)

    def test_main_do_pull_data_without_flag(self):
        expected = 1
        actual = self.mf.do_pull_data("")
        self.assertEqual(expected, actual)

    def test_main_do_pull_data_with_incorrect_flag(self):
        expected = 2
        actual = self.mf.do_pull_data("-f")
        self.assertEqual(expected, actual)

    def test_main_do_pull_data_with_d_flag(self):
        expected = 0
        actual = self.mf.do_pull_data("-d")
        self.assertEqual(expected, actual)

    def test_main_do_pull_data_with_e_flag(self):
        expected = 0
        actual = self.mf.do_pull_data("-e")
        self.assertEqual(expected, actual)

    def test_main_do_pull_data_with_d_flag_no_db(self):
        self.mf.database_name = "data_src/nonexistent.db"
        expected = 3
        actual = self.mf.do_pull_data("-d")
        self.assertEqual(expected, actual)
        self.assertRaises(FileNotFoundError)

    def test_main_do_pull_data_with_e_flag_wrong_sheet(self):
        self.mf.excel_file = "data_src/excel_file_2.xlsx"
        expected = 4
        actual = self.mf.do_pull_data("-e")
        self.assertEqual(expected, actual)
        self.assertRaises(KeyError)

    def test_main_do_push_data_without_flag(self):
        expected = 1
        actual = self.mf.do_push_data("")
        self.assertEqual(expected, actual)

    def test_main_do_push_data_with_incorrect_flag(self):
        expected = 2
        actual = self.mf.do_push_data("-f")
        self.assertEqual(expected, actual)

    def test_main_do_push_data_with_d_flag(self):
        self.mf.do_pull_data("-d")
        self.mf.database_name = "nonexistent.db"
        expected = 0
        actual = self.mf.do_push_data("-d")
        self.assertEqual(expected, actual)
        from os import remove
        remove("nonexistent.db")

    def test_main_do_push_data_with_e_flag(self):
        self.mf.excel_file = "nonexistent.xlsx"
        expected = 0
        actual = self.mf.do_push_data("-e")
        self.assertEqual(expected, actual)
        from os import remove
        remove("nonexistent.xlsx")

    def test_main_do_validate_without_flag(self):
        self.mf.do_pull_data("-d")
        expected = 0
        actual = self.mf.do_validate("")
        self.assertEqual(expected, actual)

    def test_main_do_validate_with_flag(self):
        self.mf.do_pull_data("-d")
        expected = 1
        actual = self.mf.do_validate("-f")
        self.assertEqual(expected, actual)

    def test_main_do_change_data_source_without_flag(self):
        expected_e_name = self.mf.excel_file
        expected_d_name = self.mf.database_name
        expected = 1
        actual = self.mf.do_change_data_source("")
        self.assertEqual(expected, actual)
        self.assertEqual(expected_e_name, self.mf.excel_file)
        self.assertEqual(expected_d_name, self.mf.database_name)

    def test_main_do_change_data_source_with_d_flag(self):
        expected_e_name = self.mf.excel_file
        expected_d_name = "database.db"
        expected = 0
        actual = self.mf.do_change_data_source("-d " + expected_d_name)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_d_name, self.mf.database_name)
        self.assertEqual(expected_e_name, self.mf.excel_file)

    def test_main_do_change_data_source_with_e_flag(self):
        expected_e_name = "excel.xlsx"
        expected_d_name = self.mf.database_name
        expected = 0
        actual = self.mf.do_change_data_source("-e " + expected_e_name)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_d_name, self.mf.database_name)
        self.assertEqual(expected_e_name, self.mf.excel_file)

    def test_main_do_change_data_source_with_d_flag_wrong_ext(self):
        expected_e_name = self.mf.excel_file
        expected_d_name = self.mf.database_name
        expected = 5
        actual = self.mf.do_change_data_source("-d " + "database.notdb")
        self.assertEqual(expected, actual)
        self.assertEqual(expected_d_name, self.mf.database_name)
        self.assertEqual(expected_e_name, self.mf.excel_file)

    def test_main_do_change_data_source_with_f_flag(self):
        expected_e_name = self.mf.excel_file
        expected_d_name = self.mf.database_name
        expected = 2
        actual = self.mf.do_change_data_source("-f " + expected_e_name)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_d_name, self.mf.database_name)
        self.assertEqual(expected_e_name, self.mf.excel_file)

    def test_main_do_show_data_source_without_flag(self):
        expected = 0
        actual = self.mf.do_show_data_source("")
        self.assertEqual(expected, actual)

    def test_main_do_show_data_source_with_flag(self):
        expected = 1
        actual = self.mf.do_show_data_source("-f")
        self.assertEqual(expected, actual)

    def test_main_do_save_pickle_without_flag(self):
        expected = 1
        actual = self.mf.do_save_pickle("")
        self.assertEqual(expected, actual)

    def test_main_do_save_pickle_with_flag(self):
        expected = 0
        actual = self.mf.do_save_pickle("testing_pickle")
        self.assertEqual(expected, actual)
        from os import remove
        remove("testing_pickle.pickle")

    def test_main_do_load_pickle_without_flag(self):
        expected = 1
        actual = self.mf.do_load_pickle("")
        self.assertEqual(expected, actual)

    def test_main_do_load_pickle_with_valid_flag(self):
        expected = 0
        actual = self.mf.do_load_pickle("pickle")
        self.assertEqual(expected, actual)

    def test_main_do_load_pickle_with_invalid_flag(self):
        expected = 3
        actual = self.mf.do_load_pickle("nonexistent")
        self.assertEqual(expected, actual)

    def test_main_do_graph_sales_without_flag(self):
        expected = 0
        actual = self.mf.do_graph_sales("")
        self.assertEqual(expected, actual)

    def test_main_do_graph_sales_with_flag(self):
        expected = 1
        actual = self.mf.do_graph_sales("-f")
        self.assertEqual(expected, actual)

    def test_main_do_clear_without_flag(self):
        expected = 0
        actual = self.mf.do_clear("")
        self.assertEqual(expected, actual)

    def test_main_do_clear_with_flag(self):
        expected = 1
        actual = self.mf.do_clear("-f")
        self.assertEqual(expected, actual)

    def test_main_do_quit_without_flag(self):
        with self.assertRaises(SystemExit):
            self.mf.do_quit("")

    def test_main_do_quit_with_flag(self):
        expected = 1
        actual = self.mf.do_quit("-f")
        self.assertEqual(expected, actual)

    def test_main_start(self):
        expected = 0
        actual = self.mf.start()
        self.assertEqual(expected, actual)

    # Test console_view
    def test_console_get_data(self):
        with patch('builtins.input', return_value="string"):
            actual = self.c.get_data("")
        self.assertEqual(actual, "string")

    def test_console_output(self):
        self.c.output("String")
        import sys
        self.assertEqual(sys.stdout.getvalue(), "String\n")

    # Test excel_view
    def test_excel_get_data(self):
        filename = "data_src/OfficialData.xlsx"
        self.ex.get_data(filename)
        self.assertEqual(self.ex.has_loaded_excel, True)
        self.assertEqual(self.ex.has_created_excel, False)
        self.assertEqual(self.ex.has_received_data_from_excel, True)
        self.assertEqual(self.ex.has_filled_excel, False)
        self.assertEqual(self.ex.has_saved_excel, False)

    def test_excel_output_new_file(self):
        example_data = [{
            'emp_id': 'A001',
            'gender': 'M',
            'age': 42,
            'sales': 666,
            'bmi': 'Normal',
            'salary': 180,
            'birthday': '08-07-1994',
        }]
        filename = "excel_test.xlsx"
        from os import remove
        try:
            remove(filename)
        except OSError:
            pass
        self.ex.output(example_data, filename)
        self.assertEqual(self.ex.has_loaded_excel, False)
        self.assertEqual(self.ex.has_created_excel, True)
        self.assertEqual(self.ex.has_received_data_from_excel, False)
        self.assertEqual(self.ex.has_filled_excel, True)
        self.assertEqual(self.ex.has_saved_excel, True)
        remove(filename)

    def test_excel_output_existing_file(self):
        example_data = [{
            'emp_id': 'A001',
            'gender': 'M',
            'age': 42,
            'sales': 666,
            'bmi': 'Normal',
            'salary': 180,
            'birthday': '08-07-1994',
        }]
        filename = "data_src/excel_file_2.xlsx"
        self.ex.output(example_data, filename)
        self.assertEqual(self.ex.has_loaded_excel, True)
        self.assertEqual(self.ex.has_created_excel, False)
        self.assertEqual(self.ex.has_received_data_from_excel, False)
        self.assertEqual(self.ex.has_filled_excel, True)
        self.assertEqual(self.ex.has_saved_excel, True)

if __name__ == "__main__":
    unittest.main()

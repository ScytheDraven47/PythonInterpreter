# Ben Rogers-McKee (ScytheDraven47)
# 08/03/2017
#
# ExcelView for Interpreter Program

import _sqlite3
# from view import IView
from views.view import IView


class DatabaseView(IView):

    def __init__(self):
        self.has_connected_to_db = False
        self.has_selected_data_from_db = False
        self.has_created_db_if_did_not_exist = False
        self.has_filled_db = False
        self.has_closed_db = False

    def get_data(self, db_name):
        """Gets a single row of data from the excel file, returns the data as an array"""
        import os
        if os.path.exists(db_name):
            db = self.connect_to_db(db_name)
        else:
            raise FileNotFoundError
        c = db.cursor()
        data = c.execute('''SELECT * FROM Employee''')
        self.has_selected_data_from_db = True
        all_data = data.fetchall()
        db.close()
        self.has_closed_db = True
        return all_data

    def output(self, message, db_name):
        """Loads the excel file, saves data(message) into the first empty row, saves file"""
        db = self.connect_to_db(db_name)
        c = db.cursor()
        self.create_db(c)
        for row_data in message:
            self.fill_db(db, row_data)
        db.commit()
        db.close()
        self.has_closed_db = True

    def connect_to_db(self, db_name):
        db = _sqlite3.connect(db_name)
        self.has_connected_to_db = True
        return db

    def create_db(self, cursor):
        cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
                    emp_id      VARCHAR(4) UNIQUE PRIMARY KEY,
                    gender      VARCHAR(1),
                    age         INT(2),
                    sales       INT(3),
                    bmi         VARCHAR(11),
                    salary      INT(3),
                    birthday    DATETIME
                )''')
        self.has_created_db_if_did_not_exist = True

    def fill_db(self, db, data):
        try:
            db.execute('''INSERT INTO Employee (emp_id, gender, age, sales, bmi, salary, birthday)
                        VALUES(?,?,?,?,?,?,?)''',
                       (data['emp_id'],
                        data['gender'],
                        data['age'],
                        data['sales'],
                        data['bmi'],
                        data['salary'],
                        str(data['birthday'])))
            self.has_filled_db = True
        except Exception as err:
            print(err)
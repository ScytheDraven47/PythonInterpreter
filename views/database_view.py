# Ben Rogers-McKee (ScytheDraven47)
# 08/03/2017
#
# ExcelView for Interpreter Program

import _sqlite3
from views.view import IView


class DatabaseView(IView):
    def get_data(self, db_name):
        """Gets a single row of data from the excel file, returns the data as an array"""
        db = _sqlite3.connect(db_name)
        c = db.cursor()
        data = c.execute('''SELECT * FROM Employee''')
        return data.fetchall()

    def output(self, message, db_name):
        """Loads the excel file, saves data(message) into the first empty row, saves file"""
        try:
            db = _sqlite3.connect(db_name)
        except FileNotFoundError:
            db = _sqlite3.connect(db_name)
            c = db.cursor()
            c.execute('''DROP TABLE IF EXISTS Employee''')
            c.execute('''CREATE TABLE Employee (
            emp_id      VARCHAR(4) UNIQUE PRIMARY KEY,
            gender      VARCHAR(1),
            age         INT(2),
            sales       INT(3),
            bmi         VARCHAR(11),
            salary      INT(3),
            birthday    DATETIME
            )''')
        for row_data in message:
            print(row_data)
            try:
                db.execute('''INSERT INTO Employee (emp_id, gender, age, sales, bmi, salary, birthday)
                            VALUES(?,?,?,?,?,?,?)''',
                           (row_data['emp_id'],
                            row_data['gender'],
                            row_data['age'],
                            row_data['sales'],
                            row_data['bmi'],
                            row_data['salary'],
                            str(row_data['birthday'])))
            except Exception as err:
                print(err)
        db.commit()
        db.close()

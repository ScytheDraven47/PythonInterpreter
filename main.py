# Ben Rogers-McKee (ScytheDraven47)
# 20/03/2017
#
# Main file for Interpreter project

# Imports -------------------------------------------
import cmd
from sys import argv
from datetime import datetime
from controllers.main_controller import InterpreterController
from views.database_view import DatabaseView
from views.excel_view import ExcelView
# ---------------------------------------------------

# Declaration ---------------------------------------
ic = InterpreterController()
# ---------------------------------------------------


class MainFlow(cmd.Cmd):
    excel_file = "data_src/OfficialData.xlsx"
    database_name = "data_src/db_test.db"
    prompt = "Interpreter >>>"

    # def do_add_manual_data(self, line):
    #     """
    #     Add data manually, via user input.
    #     Each piece of data will be prompted.
    #     Syntax: add_manual_data
    #     """
    #     if len(line) > 0:
    #         ic.log.output("Incorrect syntax." + str(self.do_add_manual_data.__doc__))
    #     try:
    #         ic.get_manual_data()
    #     except Exception as err:
    #         ic.log.output(err)

    def do_show_data(self, line):
        """
        Prints current held data.
        Syntax: show_data
        """
        if len(line) > 0:
            ic.log.output("Incorrect syntax." + str(self.do_show_data.__doc__))
            return 1
        else:
            ic.show_console_data()
            return 0

    def do_pull_data(self, line):
        """
        Adds data from a chosen source.
        If excel, must contain data in a sheet labelled 'input'
        Syntax: pull_data [-d|-e]
        [-d] Pulls from chosen database
        [-e] Pulls from chosen excel spreadsheet
        """
        pull_flag = self.valid_flag(line, ["-d", "-e"], 1, self.do_pull_data.__doc__)
        if type(pull_flag) is int:
            return pull_flag
        elif pull_flag == "-d":
            view = DatabaseView()
            pull_file = self.database_name
        else:
            view = ExcelView()
            pull_file = self.excel_file
        try:
            ic.get_data(pull_file, view)
            return 0
        except FileNotFoundError:
            ic.log.output("File does not exist... Please use 'change_data_source [-d|-e]' to edit data source.")
            return 3
        except KeyError:
            ic.log.output("File exists, but there is no worksheet labelled 'input'.")
            return 4

    def do_push_data(self, line):
        """
        Sends data to a chosen source.
        Syntax: push_data [-d|-e}
        [-d] Saves to chosen database
        [-e] Saves to chosen excel spreadsheet
        """
        push_flag = self.valid_flag(line, ["-d", "-e"], 1, self.do_push_data.__doc__)
        if type(push_flag) is int:
            return push_flag
        elif push_flag == "-d":
            view = DatabaseView()
            push_file = self.database_name
        else:
            view = ExcelView()
            push_file = self.excel_file
        ic.save_data(push_file, view)
        return 0

    def do_validate(self, line):
        """
        Validates current data, removing any data that is invalid.
        Syntax: validate
        """
        if len(line) == 0:
            count = ic.check()
            ic.log.output(str(count) + " counts of invalid data found.")
            return 0
        else:
            ic.log.output("Incorrect syntax." + str(self.do_validate.__doc__))
            return 1

    def do_change_data_source(self, line):
        """
        Changes the source file to save to or load from.
        Syntax: change_data_source [-d|-e] <filename.xlsx>
        [-d] changes database name (requires extension)
        [-e] changes excel file name (requires extension)
        """
        args = line.split()
        if len(args) == 2:
            cds_flag = args[0]
            filename = args[1]
            if filename.endswith(".xlsx") or filename.endswith(".db"):
                if cds_flag == "-d":
                    self.database_name = filename
                    return 0
                elif cds_flag == "-e":
                    self.excel_file = filename
                    return 0
                else:
                    ic.log.output("Invalid flag, only '-d' or '-e' are valid.")
                    return 2
            else:
                ic.log.output("Incorrect file, please use .xlsx or .db")
                return 5
        else:
            ic.log.output("Incorrect syntax." + str(self.do_change_data_source.__doc__))
            return 1

    def do_show_data_source(self, line):
        """
        Shows the source files to save to and load from.
        Syntax: show_data_source
        """
        if len(line) > 0:
            ic.log.output("Incorrect syntax." + str(self.do_show_data_source.__doc__))
            return 1
        else:
            ic.log.output("Current settings are:\n"
                          "Database Name: " + self.database_name + "\n"
                          "Excel Name: " + self.excel_file + "\n")
            return 0

    def do_save_pickle(self, line):
        """
        Saves current data inside a pickle. (no extension required)
        Syntax: save_pickle <pickle_name>
        """
        import pickle
        args = line.split()
        if len(args) == 1:
            with open(args[0]+".pickle", 'wb') as f:
                pickle.dump(ic.all_data, f)
            return 0
        else:
            ic.log.output("Incorrect syntax." + str(self.do_save_pickle.__doc__))
            return 1

    def do_load_pickle(self, line):
        """
        Loads given pickle into current data. (no extension required)
        This is a replacement, not additional.
        Syntax: load_pickle <pickle_name>
        """
        import pickle
        args = line.split()
        if len(args) == 1:
            try:
                with open(args[0]+".pickle", 'rb') as f:
                    ic.all_data = pickle.load(f)
                return 0
            except FileNotFoundError:
                ic.log.output("Pickle doesn't exist... Please type the name of an existing pickle")
                return 3
        else:
            ic.log.output("Incorrect syntax." + str(self.do_save_pickle.__doc__))
            return 1

    def do_graph_sales(self, line):
        """
        Graphs the relationship between sales and salary per employee
        Syntax: graph_sales
        """
        if len(line) == 0:
            sales = []
            salary = []
            for data in ic.all_data:
                sales.append(data['sales'])
                salary.append(data['salary'])
            import matplotlib.pyplot as plt
            plt.plot(sales, salary, 'bo')
            plt.axis([0, 999, 0, 999])
            plt.xlabel("# of Sales")
            plt.ylabel("Salary (in $1000's)")
            plt.title("Sales by salary per employee")
            # plt.show()
            return 0
        else:
            ic.log.output("Invalid syntax." + str(self.do_graph_sales.__doc__))
            return 1

    def do_clear(self, line):
        """
        Clears current held data
        Syntax: clear
        """
        if len(line) > 0:
            ic.log.output("Incorrect syntax." + str(self.do_clear.__doc__))
            return 1
        else:
            ic.all_data = []
            return 0

    def do_quit(self, line):
        """
        Quits program
        Syntax: quit
        """
        if len(line) > 0:
            ic.log.output("Incorrect syntax." + str(self.do_quit.__doc__))
            return 1
        else:
            print("Quitting...")
            raise SystemExit

    @staticmethod
    def valid_flag(line, expected_flags, expected_arg_num, error_string):
        args = line.split()
        if len(args) != expected_arg_num:
            ic.log.output("Incorrect syntax. " + error_string)
            return 1
        if args[0] in expected_flags:
            return args[0]
        else:
            ic.log.output("Invalid flag. " + error_string)
            return 2

    # Start of Interpreter CMD
    def start(self):
        ic.log.output("------- " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " -------\n"
                      "This is the python interpreter program, type 'help' for commands\n"
                      "Current settings are:\n"
                      "Database Name: " + self.database_name + "\n"
                      "Excel File: " + self.excel_file + "\n"
                      "Starting...\n")
        return 0

if __name__ == "__main__":
    m = MainFlow()
    m.start()
    # m.cmdloop()
    if len(argv) == 1:
        m.cmdloop()
    elif len(argv[:1]) == 1:
        flag = argv[1:][0]
        file = argv[1:][1]
        if flag == "-l":
            m.do_load_pickle(file)
            m.cmdloop()
        else:
            ic.log.output("Invalid flag argument. Only [-l] is valid at this time.")
    else:
        ic.log.output("Invalid command program arguments.")

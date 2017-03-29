# Ben Rogers-McKee (ScytheDraven47)
# 08/03/2017
#
# ConsoleView for Interpreter Program

from views.view import IView


class ConsoleView(IView):
    def get_data(self, message):
        """Returns raw user input"""
        result = input("{}: ".format(message))
        return result

    def output(self, message, optional=None):
        """Prints message"""
        print(message)

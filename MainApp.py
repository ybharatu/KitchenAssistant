from pymongo import MongoClient
from KitchenFunctions import *
from PyQt5 import QtCore, QtGui, QtWidgets
from KitchenAppGUI import *
from multiprocessing import Process
import storage


class KitchenApp( QtWidgets.QMainWindow, Ui_MainWindow):

    # Init Function
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Button connections


# Main Driving Function
if __name__ == "__main__":

    # Varable to signal process 2 to end
    StillRunning = 1

    # Enable Mongo Client
    client = MongoClient('localhost', 27017, connect=False)

    # Create Database
    db = client['Ingredients']

    # Create Database list
    food = db.food

    # Create and start Email Notification Process
    #EmailNotifyP = Process(target=EmailNotifyRun, args=(StillRunning,food))
    #EmailNotifyP.start()

    # Create GUI Form
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = KitchenApp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    while True:
        # Asks user for command and formats for parsing
        cmd = input("Command: ")
        cmd = cmd.strip().lower()

        # Parses command
        if cmd == "add":
            add_item(food, cmd)
        elif cmd == "print" or cmd == "ls":
            print_items(food, cmd)
        elif cmd == "remove":
            remove_item(food, cmd)
        elif cmd == "update":
            update_item(food, cmd)
        elif cmd == "recipes":
            search_recipe_by_ingredients(food)
        elif cmd == "quit" or cmd == "exit" or cmd == "q":
            StillRunning = 0
            break
        else:
            # TODO: Should have a -h or -verbose option
            print("Not a valid command")

    # Ends Email Notify Process TODO: Look into Daemon Processes
    #EmailNotifyP.terminate()




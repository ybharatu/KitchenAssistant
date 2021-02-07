from pymongo import MongoClient
from KitchenFunctions import *
from PyQt5 import QtCore, QtGui, QtWidgets
from KitchenAppGUI import *
from multiprocessing import Process
import storage


class KitchenApp( QtWidgets.QMainWindow, Ui_MainWindow):

    # Init Function
    def __init__(self, parent=None):
        #super().__init__(parent)
        super(KitchenApp, self).__init__(parent)
        self.setupUi(self)

        # Text Edit size adjustments (TextEdit cannot vertically align (REALLY STUPID))
        margin = 2
        self.NameTextEdit.document().setDocumentMargin(margin)
        fontMetrics = QtGui.QFontMetrics(self.NameTextEdit.font())
        height = fontMetrics.height() + (margin + self.NameTextEdit.frameWidth()) * 2
        self.NameTextEdit.setFixedHeight(height)

        # Button connections
        self.addButton.clicked.connect(self.addPage)
        self.AddItemButton.clicked.connect(self.addItem)
        self.dataButton.clicked.connect(self.changeDataFrame)
        self.homeButton.clicked.connect(self.changeHomeFrame)
        # self.downloadButton.clicked.connect(self.downloadResults)
        self.removeButton.clicked.connect(self.removeItem)

    def changeDataFrame(self):
        print("Changed to Data frame")
        self.stackedWidget.setCurrentIndex(1)

    def changeHomeFrame(self):
        print("Changed to Home frame")
        self.stackedWidget.setCurrentIndex(0)

    def addPage(self):
        print("Changed to Add Item Page")
        self.stackedWidget.setCurrentIndex(2)
        return

    def addItem(self):
        return

    def downloadResults(self):
        return

    def removeItem(self):
        return

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
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = KitchenApp()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())

    currentApp = QtWidgets.QApplication(sys.argv)
    currentForm = KitchenApp()

    currentForm.show()
    currentApp.exec_()

    while False:
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




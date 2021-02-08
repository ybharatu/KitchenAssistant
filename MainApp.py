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
        margin = 10
        self.NameTextEdit.document().setDocumentMargin(margin)
        fontMetrics = QtGui.QFontMetrics(self.NameTextEdit.font())
        height = fontMetrics.height() + (margin + self.NameTextEdit.frameWidth()) * 2
        self.NameTextEdit.setFixedHeight(height)
        self.QuantityTextEdit.document().setDocumentMargin(margin)
        height = fontMetrics.height() + (margin + self.QuantityTextEdit.frameWidth()) * 2
        self.QuantityTextEdit.setFixedHeight(height)
        self.ExpireTextEdit.document().setDocumentMargin(margin)
        height = fontMetrics.height() + (margin + self.ExpireTextEdit.frameWidth()) * 2
        self.ExpireTextEdit.setFixedHeight(height)

        # Button connections
        self.addButton.clicked.connect(self.addPage)
        self.AddItemButton.clicked.connect(self.addItem)
        self.dataButton.clicked.connect(self.changeDataFrame)
        self.homeButton.clicked.connect(self.changeHomeFrame)
        self.downloadButton.clicked.connect(self.downloadResults)
        self.removeItemButton.clicked.connect(self.removeItem)
        self.removeButton.clicked.connect(self.removePage)

        # Set up Initial Table
        self.initTable()

        # Set up checkboxes in remove Item screen
        self.checks = []
        self.initRemoveList()

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

    def resetItemForm(self):
        self.NameTextEdit.setText("")
        self.QuantityTextEdit.setText("")
        self.ExpireTextEdit.setText("")

    def addItem(self):
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row + 1)
        col = 0

        if self.NameTextEdit.toPlainText() != "" and self.QuantityTextEdit.toPlainText() != "":
            row_data = [self.NameTextEdit.toPlainText(), self.QuantityTextEdit.toPlainText(), self.ExpireTextEdit.toPlainText()]
            gui_add_item(food,self.NameTextEdit.toPlainText(),self.QuantityTextEdit.toPlainText(),self.ExpireTextEdit.toPlainText())
        else:
            print("Not all values")
            return

        for item in row_data:
            cell = QtWidgets.QTableWidgetItem(str(item))
            cell.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
            self.tableWidget.setItem(row, col, cell)
            col += 1
        self.resetItemForm()
        self.changeDataFrame()

    def initTable(self):
        # Iterates through all items in database list and sets up table
        for entry in food.find():
            row = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(row + 1)
            col = 0
            name = entry.get("name")
            quantity = entry.get("quantity")
            expire = entry.get("expire")
            row_data = [name, quantity, expire]
            for item in row_data:
                cell = QtWidgets.QTableWidgetItem(str(item))
                cell.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
                self.tableWidget.setItem(row, col, cell)
                col += 1

    def initRemoveList(self):

        for entry in food.find():
            print(entry.get("name"))
            check = QtWidgets.QCheckBox()

            check.setText(entry.get("name"))
            self.verticalLayout.addWidget(check)
            if len(self.checks) != 0:
                newHeight = self.checks[-1].geometry().height() + 1 * len(self.checks)  # Compensate for new checkbox
                check.resize(self.geometry().width(), newHeight)
            self.checks.append(check)


    def downloadResults(self):
        return

    def removeItem(self):
        to_remove = []
        for box in self.checks:
            if box.isChecked():
                to_remove.append(box)

        for rem in to_remove:
            item_name = rem.text()
            #print(item_name)
            gui_remove_item(food, item_name)
            self.verticalLayout.removeWidget(rem)
            self.checks.remove(rem)

        for box in self.checks:
            self.verticalLayout.removeWidget(box)
            box.deleteLater()

        self.checks = []
        self.initRemoveList()

    def removePage(self):
        print("Changed to Remove Page")
        self.stackedWidget.setCurrentIndex(3)

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




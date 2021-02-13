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
        self.recipeButton.clicked.connect(self.recipePage)
        self.recipe1Button.clicked.connect(lambda: self.showRecipe(0))
        self.recipe2Button.clicked.connect(lambda: self.showRecipe(1))
        self.recipe3Button.clicked.connect(lambda: self.showRecipe(2))


        # Set up Initial Table
        self.initTable()

        # Set up checkboxes in remove Item screen
        self.checks = []
        self.to_remove = []

        # Veriables for recipes
        self.recipes = []
        # Recipe display status. 0 -> not shown, 1 -> recipe 1, 2 -> recipe 2, 3 -> recipe 3
        self.recipe_status = 0

    # Changes screen to table view
    def changeDataFrame(self):
        print("Changed to Data frame")
        self.stackedWidget.setCurrentIndex(1)

    # Changes screen to Home view
    def changeHomeFrame(self):
        print("Changed to Home frame")
        self.stackedWidget.setCurrentIndex(0)

    # Changes screen to Add item view
    def addPage(self):
        print("Changed to Add Item Page")
        self.stackedWidget.setCurrentIndex(2)
        return

    # Gets rid of existing text in add item script
    def resetItemForm(self):
        self.NameTextEdit.setText("")
        self.QuantityTextEdit.setText("")
        self.ExpireTextEdit.setText("")

    # Adds item to Food database and Table
    def addItem(self):

        # Init row and col numbers
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row + 1)
        col = 0

        # If name and quantity exists, create new row and add item to database
        if self.NameTextEdit.toPlainText() != "" and self.QuantityTextEdit.toPlainText() != "":
            row_data = [self.NameTextEdit.toPlainText(), self.QuantityTextEdit.toPlainText(), self.ExpireTextEdit.toPlainText()]
            gui_add_item(food, self.NameTextEdit.toPlainText(), self.QuantityTextEdit.toPlainText(), self.ExpireTextEdit.toPlainText())
        # TODO: Need to do something if needed values aren't entered
        else:
            print("Not all values")
            return

        # Iterates through row_data (name, quantity, and expiration date)
        for item in row_data:
            cell = QtWidgets.QTableWidgetItem(str(item))
            cell.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
            self.tableWidget.setItem(row, col, cell)
            col += 1

        # Need to reset the form to prevent text from persisting
        self.resetItemForm()
        self.changeDataFrame()

    # Initializes Table with all food in database
    def initTable(self):
        # Iterates through all items in database list and sets up table
        for entry in food.find():
            # Sets up initial row and col numbers
            row = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(row + 1)
            col = 0

            # Initializes row_data
            name = entry.get("name")
            quantity = entry.get("quantity")
            expire = entry.get("expire")
            row_data = [name, quantity, expire]

            # Iterates each item for each entry and fills the table
            for item in row_data:
                cell = QtWidgets.QTableWidgetItem(str(item))
                cell.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
                self.tableWidget.setItem(row, col, cell)
                col += 1

    # Updating the table with added and removed items
    def updateTable(self):

        # Iterates through rows of the table
        for row in range(1,self.tableWidget.rowCount()):
            # Iterates through items selected to be removed
            for rem in self.to_remove:
                print("Does " + self.tableWidget.item(row,0).text() + " == " + rem.text() + " ???")
                # Remove row from table if names match
                if self.tableWidget.item(row,0).text() == rem.text():
                    self.tableWidget.removeRow(row)
                    self.to_remove.remove(rem)
                    break

    # Initializes the Remove list
    def initRemoveList(self):
        # Iterates through all food in database
        for entry in food.find():
            # Creates checkbox object
            check = QtWidgets.QCheckBox()
            check.setText(entry.get("name"))

            # Adds object to view
            self.verticalLayout.addWidget(check)
            # Adjusts position of subsequent items
            if len(self.checks) != 0:
                newHeight = self.checks[-1].geometry().height() + 1 * len(self.checks)  # Compensate for new checkbox
                check.resize(self.geometry().width(), newHeight)
            # Updates list of all checkbox objects
            self.checks.append(check)

    # TODO: Downloads csv file of food list
    def downloadResults(self):
        return

    # Removes items from database
    def removeItem(self):
        # Iterates through checkboxes to record selected boxes
        for box in self.checks:
            if box.isChecked():
                self.to_remove.append(box)

        # Removes item from database and checkbox
        for rem in self.to_remove:
            item_name = rem.text()
            gui_remove_item(food, item_name)
            rem.setChecked(False)
            rem.deleteLater()
            self.verticalLayout.removeWidget(rem)
            self.checks.remove(rem)

        # Remove all checkboxes
        for box in self.checks:
            self.verticalLayout.removeWidget(box)
            box.deleteLater()
            del box

        self.checks = []
        self.updateTable()
        self.changeDataFrame()

    # Changes screen to Remove item view
    def removePage(self):
        print("Changed to Remove Page")
        self.initRemoveList()
        self.stackedWidget.setCurrentIndex(3)

    # Changes screen to Recipe view
    def recipePage(self):
        print("Changed to Recipe Page")
        if len(self.recipes) == 0:
            self.initRecipePage()
        self.stackedWidget.setCurrentIndex(4)

    # Initializes Recipe page by searching for 3 recipes
    def initRecipePage(self):

        # Get 3 recipes
        self.recipes = gui_search_recipe_by_ingredients ( food )

        # Populate 3 buttons with 3 recipes
        self.recipe1Button.setText(self.recipes[0]['title'])
        self.recipe2Button.setText(self.recipes[1]['title'])
        self.recipe3Button.setText(self.recipes[2]['title'])

    # Displays individual recipe information
    def showRecipe(self,num):

        # Check if there are no recipes or the same recipe requested to avoid api calls
        print("Does recipe_status = " + str(self.recipe_status) + " == " + str(num+1) + " ?")
        if self.recipe_status != 0 and self.recipe_status == num + 1:
            # Changed frame to Individual recipe view
            self.stackedWidget.setCurrentIndex(5)
            return

        # Set to the appropriate recipe
        recipe = self.recipes[num]
        self.recipe_status = num + 1

        # Cleans any existing items in the table
        self.ingrediantList.clear()
        self.instructionList.clear()

        # Set Title label to name of recipe TODO: Need to make sure label resizes or changes the font if too large
        self.recipeNameLabel.setText(recipe['title'])

        # Get used and missing ingredients
        miss_ingred = gui_get_missing_ingredients(recipe)
        used_ingred = gui_get_used_ingredients(recipe)

        # Get step by step instructions
        instr = gui_get_instructions(recipe)

        # Iterate through used ingredients and add to list as green
        for ingred in used_ingred:
            list_item = QtWidgets.QListWidgetItem(ingred)
            list_item.setForeground(QtGui.QBrush(QtGui.QColor(33, 255, 6)))
            self.ingrediantList.addItem(list_item)

        # Iterate through missing ingredients and add to list as red
        for ingred in miss_ingred:
            list_item = QtWidgets.QListWidgetItem(ingred)
            list_item.setForeground(QtGui.QBrush(QtGui.QColor(252, 1, 7)))
            self.ingrediantList.addItem(list_item)

        # Iterate through instructions and add to list
        for inst in instr:
            list_item = QtWidgets.QListWidgetItem(inst)
            list_item.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
            self.instructionList.addItem(list_item)

        # Changed frame to Individual recipe view
        self.stackedWidget.setCurrentIndex(5)


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




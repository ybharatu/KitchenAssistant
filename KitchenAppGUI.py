# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KitchenAppGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 532)
        MainWindow.setStyleSheet("background-color: rgb(17, 17, 18)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 71, 581))
        self.frame.setStyleSheet("background-color: rgb(14, 13, 14)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.homeButton = QtWidgets.QPushButton(self.frame)
        self.homeButton.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.homeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui_images/home_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("gui_images/home_color.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QtCore.QSize(50, 50))
        self.homeButton.setObjectName("homeButton")
        self.dataButton = QtWidgets.QPushButton(self.frame)
        self.dataButton.setGeometry(QtCore.QRect(0, 70, 71, 71))
        self.dataButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("gui_images/Table5_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dataButton.setIcon(icon1)
        self.dataButton.setIconSize(QtCore.QSize(50, 50))
        self.dataButton.setObjectName("dataButton")
        self.saveButton = QtWidgets.QPushButton(self.frame)
        self.saveButton.setGeometry(QtCore.QRect(0, 280, 71, 71))
        self.saveButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("gui_images/save_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon2)
        self.saveButton.setIconSize(QtCore.QSize(50, 50))
        self.saveButton.setObjectName("saveButton")
        self.downloadButton = QtWidgets.QPushButton(self.frame)
        self.downloadButton.setGeometry(QtCore.QRect(0, 210, 71, 71))
        self.downloadButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("gui_images/download_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon3)
        self.downloadButton.setIconSize(QtCore.QSize(50, 50))
        self.downloadButton.setObjectName("downloadButton")
        self.recipeButton = QtWidgets.QPushButton(self.frame)
        self.recipeButton.setGeometry(QtCore.QRect(0, 140, 71, 71))
        self.recipeButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("gui_images/star_new_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recipeButton.setIcon(icon4)
        self.recipeButton.setIconSize(QtCore.QSize(50, 50))
        self.recipeButton.setObjectName("recipeButton")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(70, 0, 731, 551))
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.welcomeLabel = QtWidgets.QLabel(self.homePage)
        self.welcomeLabel.setGeometry(QtCore.QRect(0, 0, 721, 191))
        font = QtGui.QFont()
        font.setFamily("Muna")
        font.setPointSize(39)
        font.setBold(False)
        font.setWeight(50)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setStyleSheet("color: rgb(112, 0, 255)")
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.stackedWidget.addWidget(self.homePage)
        self.tablePage = QtWidgets.QWidget()
        self.tablePage.setStyleSheet("")
        self.tablePage.setObjectName("tablePage")
        self.tableWidget = QtWidgets.QTableWidget(self.tablePage)
        self.tableWidget.setGeometry(QtCore.QRect(0, 120, 731, 361))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QHeaderView::section { background-color:RGB(17,17,18);color: rgb(112, 0, 255)}")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(243)
        self.label_2 = QtWidgets.QLabel(self.tablePage)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 721, 111))
        font = QtGui.QFont()
        font.setFamily("Muna")
        font.setPointSize(39)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(112, 0, 255)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.addButton = QtWidgets.QPushButton(self.tablePage)
        self.addButton.setGeometry(QtCore.QRect(150, 480, 71, 71))
        self.addButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("gui_images/plus_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon5)
        self.addButton.setIconSize(QtCore.QSize(50, 50))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.tablePage)
        self.removeButton.setGeometry(QtCore.QRect(480, 480, 71, 71))
        self.removeButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("gui_images/minus_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeButton.setIcon(icon6)
        self.removeButton.setIconSize(QtCore.QSize(50, 50))
        self.removeButton.setObjectName("removeButton")
        self.stackedWidget.addWidget(self.tablePage)
        self.AddItemPage = QtWidgets.QWidget()
        self.AddItemPage.setObjectName("AddItemPage")
        self.label_3 = QtWidgets.QLabel(self.AddItemPage)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 721, 111))
        font = QtGui.QFont()
        font.setFamily("Muna")
        font.setPointSize(39)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(112, 0, 255)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.NameTextEdit = QtWidgets.QTextEdit(self.AddItemPage)
        self.NameTextEdit.setGeometry(QtCore.QRect(220, 210, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NameTextEdit.setFont(font)
        self.NameTextEdit.setStyleSheet("background-color: rgb(14, 13, 14);\n"
"color: rgb(255, 255, 255)")
        self.NameTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.NameTextEdit.setObjectName("NameTextEdit")
        self.QuantityTextEdit = QtWidgets.QTextEdit(self.AddItemPage)
        self.QuantityTextEdit.setGeometry(QtCore.QRect(220, 260, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QuantityTextEdit.setFont(font)
        self.QuantityTextEdit.setStyleSheet("background-color: rgb(14, 13, 14);\n"
"color: rgb(255,255,255)")
        self.QuantityTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.QuantityTextEdit.setObjectName("QuantityTextEdit")
        self.ExpireTextEdit = QtWidgets.QTextEdit(self.AddItemPage)
        self.ExpireTextEdit.setGeometry(QtCore.QRect(220, 310, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ExpireTextEdit.setFont(font)
        self.ExpireTextEdit.setStyleSheet("background-color: rgb(14, 13, 14);\n"
"color: rgb(255,255,255)")
        self.ExpireTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ExpireTextEdit.setObjectName("ExpireTextEdit")
        self.NameLabel = QtWidgets.QLabel(self.AddItemPage)
        self.NameLabel.setGeometry(QtCore.QRect(150, 220, 61, 21))
        self.NameLabel.setStyleSheet("color: rgb(112, 0, 255)")
        self.NameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NameLabel.setObjectName("NameLabel")
        self.QuantityLabel = QtWidgets.QLabel(self.AddItemPage)
        self.QuantityLabel.setGeometry(QtCore.QRect(150, 270, 61, 21))
        self.QuantityLabel.setStyleSheet("color: rgb(112, 0, 255)")
        self.QuantityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.QuantityLabel.setObjectName("QuantityLabel")
        self.expirationLabel = QtWidgets.QLabel(self.AddItemPage)
        self.expirationLabel.setGeometry(QtCore.QRect(150, 320, 61, 21))
        self.expirationLabel.setStyleSheet("color: rgb(112, 0, 255)")
        self.expirationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.expirationLabel.setObjectName("expirationLabel")
        self.AddItemButton = QtWidgets.QPushButton(self.AddItemPage)
        self.AddItemButton.setGeometry(QtCore.QRect(330, 390, 71, 71))
        self.AddItemButton.setText("")
        self.AddItemButton.setIcon(icon5)
        self.AddItemButton.setIconSize(QtCore.QSize(50, 50))
        self.AddItemButton.setObjectName("AddItemButton")
        self.stackedWidget.addWidget(self.AddItemPage)
        self.removeItemPage = QtWidgets.QWidget()
        self.removeItemPage.setObjectName("removeItemPage")
        self.label_7 = QtWidgets.QLabel(self.removeItemPage)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 721, 111))
        font = QtGui.QFont()
        font.setFamily("Muna")
        font.setPointSize(39)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(112, 0, 255)")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.removeItemButton = QtWidgets.QPushButton(self.removeItemPage)
        self.removeItemButton.setGeometry(QtCore.QRect(310, 450, 71, 71))
        self.removeItemButton.setText("")
        self.removeItemButton.setIcon(icon6)
        self.removeItemButton.setIconSize(QtCore.QSize(50, 50))
        self.removeItemButton.setObjectName("removeItemButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.removeItemPage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 150, 601, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget.addWidget(self.removeItemPage)
        self.recipeListPage = QtWidgets.QWidget()
        self.recipeListPage.setObjectName("recipeListPage")
        self.refreshButton = QtWidgets.QPushButton(self.recipeListPage)
        self.refreshButton.setGeometry(QtCore.QRect(300, 420, 71, 71))
        self.refreshButton.setStyleSheet("background-color: rgb(17, 17, 18)")
        self.refreshButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("gui_images/refresh_color-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshButton.setIcon(icon7)
        self.refreshButton.setIconSize(QtCore.QSize(50, 50))
        self.refreshButton.setObjectName("refreshButton")
        self.recipe1Button = QtWidgets.QPushButton(self.recipeListPage)
        self.recipe1Button.setGeometry(QtCore.QRect(80, 90, 491, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.recipe1Button.setFont(font)
        self.recipe1Button.setStyleSheet("background-color:rgba(0,0,0,100)")
        self.recipe1Button.setText("")
        self.recipe1Button.setObjectName("recipe1Button")
        self.recipe2Button = QtWidgets.QPushButton(self.recipeListPage)
        self.recipe2Button.setGeometry(QtCore.QRect(80, 200, 491, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.recipe2Button.setFont(font)
        self.recipe2Button.setStyleSheet("background-color:rgba(0,0,0,100)")
        self.recipe2Button.setText("")
        self.recipe2Button.setObjectName("recipe2Button")
        self.recipe3Button = QtWidgets.QPushButton(self.recipeListPage)
        self.recipe3Button.setGeometry(QtCore.QRect(80, 310, 491, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.recipe3Button.setFont(font)
        self.recipe3Button.setStyleSheet("background-color:rgba(0, 0, 0,100)")
        self.recipe3Button.setText("")
        self.recipe3Button.setObjectName("recipe3Button")
        self.recipe1Label = QtWidgets.QLabel(self.recipeListPage)
        self.recipe1Label.setGeometry(QtCore.QRect(90, 100, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.recipe1Label.setFont(font)
        self.recipe1Label.setStyleSheet("color: rgb(255,255,255)")
        self.recipe1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.recipe1Label.setWordWrap(True)
        self.recipe1Label.setObjectName("recipe1Label")
        self.recipe2Label = QtWidgets.QLabel(self.recipeListPage)
        self.recipe2Label.setGeometry(QtCore.QRect(90, 210, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.recipe2Label.setFont(font)
        self.recipe2Label.setStyleSheet("color: rgb(255,255,255)")
        self.recipe2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.recipe2Label.setWordWrap(True)
        self.recipe2Label.setObjectName("recipe2Label")
        self.recipe3Label = QtWidgets.QLabel(self.recipeListPage)
        self.recipe3Label.setGeometry(QtCore.QRect(90, 320, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.recipe3Label.setFont(font)
        self.recipe3Label.setStyleSheet("color: rgb(255,255,255)")
        self.recipe3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.recipe3Label.setWordWrap(True)
        self.recipe3Label.setObjectName("recipe3Label")
        self.recipe3Label.raise_()
        self.recipe2Label.raise_()
        self.refreshButton.raise_()
        self.recipe2Button.raise_()
        self.recipe3Button.raise_()
        self.recipe1Label.raise_()
        self.recipe1Button.raise_()
        self.stackedWidget.addWidget(self.recipeListPage)
        self.recipeViewPage = QtWidgets.QWidget()
        self.recipeViewPage.setObjectName("recipeViewPage")
        self.recipeNameLabel = QtWidgets.QLabel(self.recipeViewPage)
        self.recipeNameLabel.setGeometry(QtCore.QRect(60, 20, 561, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.recipeNameLabel.setFont(font)
        self.recipeNameLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.recipeNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.recipeNameLabel.setWordWrap(True)
        self.recipeNameLabel.setObjectName("recipeNameLabel")
        self.ingrediantList = QtWidgets.QListWidget(self.recipeViewPage)
        self.ingrediantList.setGeometry(QtCore.QRect(60, 150, 256, 341))
        self.ingrediantList.setStyleSheet("color: rgb(255,255,255)")
        self.ingrediantList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ingrediantList.setProperty("isWrapping", False)
        self.ingrediantList.setWordWrap(True)
        self.ingrediantList.setObjectName("ingrediantList")
        self.instructionList = QtWidgets.QListWidget(self.recipeViewPage)
        self.instructionList.setGeometry(QtCore.QRect(370, 150, 256, 341))
        self.instructionList.setStyleSheet("color: rgb(255,255,255)")
        self.instructionList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.instructionList.setProperty("isWrapping", False)
        self.instructionList.setWordWrap(True)
        self.instructionList.setObjectName("instructionList")
        self.ingrediantLabel = QtWidgets.QLabel(self.recipeViewPage)
        self.ingrediantLabel.setGeometry(QtCore.QRect(60, 110, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ingrediantLabel.setFont(font)
        self.ingrediantLabel.setStyleSheet("color:rgb(255,255,255)")
        self.ingrediantLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ingrediantLabel.setObjectName("ingrediantLabel")
        self.instructionLabel = QtWidgets.QLabel(self.recipeViewPage)
        self.instructionLabel.setGeometry(QtCore.QRect(370, 110, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.instructionLabel.setFont(font)
        self.instructionLabel.setStyleSheet("color:rgb(255,255,255)")
        self.instructionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionLabel.setObjectName("instructionLabel")
        self.stackedWidget.addWidget(self.recipeViewPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcomeLabel.setText(_translate("MainWindow", "Welcome to Kitchen Assistant"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Expiration"))
        self.label_2.setText(_translate("MainWindow", "Table View"))
        self.label_3.setText(_translate("MainWindow", "ADD ITEM"))
        self.NameLabel.setText(_translate("MainWindow", "Name"))
        self.QuantityLabel.setText(_translate("MainWindow", "Quantity"))
        self.expirationLabel.setText(_translate("MainWindow", "Expiration"))
        self.label_7.setText(_translate("MainWindow", "Remove Item(s)"))
        self.recipe1Label.setText(_translate("MainWindow", "Recipe 1"))
        self.recipe2Label.setText(_translate("MainWindow", "Recipe 2"))
        self.recipe3Label.setText(_translate("MainWindow", "Recipe 3"))
        self.recipeNameLabel.setText(_translate("MainWindow", "Recipe Name"))
        self.ingrediantLabel.setText(_translate("MainWindow", "Ingrediants"))
        self.instructionLabel.setText(_translate("MainWindow", "Instructions"))

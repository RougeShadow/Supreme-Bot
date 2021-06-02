# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelCopBot.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  #spawns the main window we will be putting everything in
        MainWindow.resize(522, 414) #we set the size of the window
        self.centralwidget = QtWidgets.QWidget(MainWindow) # spawns widget so we can add others to it
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget) #allows us to add text feild
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 80, 231, 31)) #set the size of the text feild
        self.plainTextEdit.setObjectName("plainTextEdit")  #give the object a name so we can interact with it easily
        self.pushButton = QtWidgets.QPushButton(self.centralwidget) # spawns a button
        self.pushButton.setGeometry(QtCore.QRect(200, 330, 75, 23)) #we set the sizing and postition
        self.pushButton.setObjectName("pushButton") #give the button a name so we may interact with it
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget) #allows us to add text feild
        self.textEdit.setGeometry(QtCore.QRect(130, 200, 231, 31)) #we set the sizing and postition
        self.textEdit.setObjectName("textEdit")#give the object a name so we can interact with it easily
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget) #allows us to add text feild
        self.textEdit_2.setGeometry(QtCore.QRect(10, 130, 231, 31))#we set the sizing and postition
        self.textEdit_2.setObjectName("textEdit_2")#give the object a name so we can interact with it easily
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)#spawns a progress bar
        self.progressBar.setGeometry(QtCore.QRect(10, 300, 511, 23))#we set the sizing and postition
        self.progressBar.setProperty("value", 24) #gives the progress bar a starting value that will go up as progress is made
        self.progressBar.setObjectName("progressBar")#give the object a name so we can interact with it easily
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget) #allows us to add text feild
        self.textEdit_3.setGeometry(QtCore.QRect(260, 80, 231, 31))#we set the sizing and postition
        self.textEdit_3.setObjectName("textEdit_3")#give the object a name so we can interact with it easily
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget) #allows us to add text feild
        self.plainTextEdit_2.setGeometry(QtCore.QRect(260, 130, 231, 31))#we set the sizing and postition
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")#give the object a name so we can interact with it easily
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget) #allows us to add text feild
        self.textEdit_4.setGeometry(QtCore.QRect(10, 20, 231, 31))#we set the sizing and postition
        self.textEdit_4.setObjectName("textEdit_4")#give the object a name so we can interact with it easily
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget) #allows us to add text feild
        self.textEdit_5.setGeometry(QtCore.QRect(260, 20, 231, 31))#we set the sizing and postition
        self.textEdit_5.setObjectName("textEdit_5")#give the object a name so we can interact with it easily
        self.label = QtWidgets.QLabel(self.centralwidget) #creates a label for the fields
        self.label.setGeometry(QtCore.QRect(10, 0, 46, 13))#we set the sizing and postition
        self.label.setObjectName("label")#give the object a name so we can interact with it easily
        self.label_2 = QtWidgets.QLabel(self.centralwidget) #creates a label for the fields
        self.label_2.setGeometry(QtCore.QRect(10, 60, 46, 13))#we set the sizing and postition
        self.label_2.setObjectName("label_2")#give the object a name so we can interact with it easily
        self.label_3 = QtWidgets.QLabel(self.centralwidget) #creates a label for the fields
        self.label_3.setGeometry(QtCore.QRect(210, 180, 71, 16))#we set the sizing and postition
        self.label_3.setObjectName("label_3")#give the object a name so we can interact with it easily
        self.label_4 = QtWidgets.QLabel(self.centralwidget)#creates a label for the fields
        self.label_4.setGeometry(QtCore.QRect(10, 110, 46, 13))#we set the sizing and postition
        self.label_4.setObjectName("label_4")#give the object a name so we can interact with it easily
        self.label_5 = QtWidgets.QLabel(self.centralwidget)#creates a label for the fields
        self.label_5.setGeometry(QtCore.QRect(260, 0, 46, 13))#we set the sizing and postition
        self.label_5.setObjectName("label_5")#give the object a name so we can interact with it easily
        self.label_6 = QtWidgets.QLabel(self.centralwidget)#creates a label for the fields
        self.label_6.setGeometry(QtCore.QRect(260, 60, 71, 16))#we set the sizing and postition
        self.label_6.setObjectName("label_6")#give the object a name so we can interact with it easily
        self.label_7 = QtWidgets.QLabel(self.centralwidget)#creates a label for the fields
        self.label_7.setGeometry(QtCore.QRect(260, 110, 46, 13))#we set the sizing and postition
        self.label_7.setObjectName("label_7")#give the object a name so we can interact with it easily
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)# spawns a button
        self.pushButton_2.setGeometry(QtCore.QRect(20, 250, 75, 23))#we set the sizing and postition
        self.pushButton_2.setObjectName("pushButton_2")#give the button a name so we may interact with it
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)# spawns a button
        self.pushButton_3.setGeometry(QtCore.QRect(200, 250, 75, 23))#we set the sizing and postition
        self.pushButton_3.setObjectName("pushButton_3") #give the button a name so we may interact with it
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)# spawns a button
        self.pushButton_4.setGeometry(QtCore.QRect(360, 250, 75, 23))#we set the sizing and postition
        self.pushButton_4.setObjectName("pushButton_4") #give the button a name so we may interact with it
        MainWindow.setCentralWidget(self.centralwidget) # the main window counts as a widget so we had to spawn it here
        self.menubar = QtWidgets.QMenuBar(MainWindow) #spawns a menu
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 21))#we set the sizing and postition
        self.menubar.setObjectName("menubar")#give the object a name so we can interact with it
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) #connects the widgets to their names so something happens when we interact with them

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start")) #sets the button to a value of start
        self.label.setText(_translate("MainWindow", "Gmail")) #sets label as gmaill
        self.label_2.setText(_translate("MainWindow", "Password")) #sets label as password
        self.label_3.setText(_translate("MainWindow", "Card Number")) #sets label as card number
        self.label_4.setText(_translate("MainWindow", "CVV")) #sets label as CVV
        self.label_5.setText(_translate("MainWindow", "Expiry")) #sets label as expiry
        self.label_6.setText(_translate("MainWindow", "Type of Cloth")) #sets label as Type of Cloth
        self.label_7.setText(_translate("MainWindow", "Product")) #sets label as item
        self.pushButton_2.setText(_translate("MainWindow", "SNKRS")) #sets button as SNKRS
        self.pushButton_3.setText(_translate("MainWindow", "Supreme")) #sets button as SNKRS
        self.pushButton_4.setText(_translate("MainWindow", "Footlocker")) #sets button as SNKRS
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
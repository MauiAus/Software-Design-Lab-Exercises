'''
Made by Mark Austin L. Pagarigan
04/12/2020
'''

from oauth2client.service_account import ServiceAccountCredentials
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QGroupBox, QPushButton, QFormLayout, QLabel, QWidget, QStackedWidget, QApplication
from PyQt5.QtGui import QIcon
import gspread
import pandas as pd
from datetime import date
import time
from datetime import datetime

class loginData:
    user = ["Mark", "Marielle", "Ana"]
    password = ["123", "321", "312"]

    def __init__(self, userw, passw):
        self.userw = userw
        self.passw = passw

    def matchUser(self):
        if self.userw in self.user:
            return True
        else:
            return False

    def matchPass(self):
        if self.passw in self.password:
            return True
        else:
            return False

    def AccMatch(self):
        if (self.matchUser() and self.matchPass() == True):
            if self.user.index(self.userw) == self.password.index(self.passw):
                return True
            else:
                return False
        else:
            return False

    def MatchAcc(self):
        if (self.AccMatch() == True):
            return True
        else:
            return False

class SharedCell:
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('ChatSheets-fd6bda5a235e.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open('ChatSheets').sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    def refreshData(self):
        self.data = self.sheet.get_all_records()
        self.df = pd.DataFrame(self.data)
    def getDate(self):
        return date.today().strftime("%m/%d/%y")
    def getTime(self):
        return time.strftime("%H:%M:%S", time.localtime())
    def getMaxSheetIndex(self):
        return self.df.last_valid_index()
    def printTest(self):
        print(self.df.sort_values('name'))
    def addMessage(self, name, message):
        self.refreshData()
        new_row = [name, message, self.getDate(), self.getTime()]
        print(self.getMaxSheetIndex())
        if self.getMaxSheetIndex() == None:
            self.sheet.insert_row(new_row, 2)
            print('exception ran')
        else:
            self.sheet.insert_row(new_row, self.getMaxSheetIndex()+3)
            print("this ran")
    def loadName(self, i):
        return self.df.iloc[i,0]
    def loadMessage(self, i):
        return self.df.iloc[i,1]
    def loadDate(self,i):
        return self.df.iloc[i,2]
    def loadTime(self,i):
        return self.df.iloc[i,3]
    def loadNameHead(self, i):
        return str(self.loadName(i) + ' ' + self.loadDate(i) + ' '+ self.loadTime(i))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(287, 243)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Signin = QtWidgets.QLabel(self.centralwidget)
        self.Signin.setGeometry(QtCore.QRect(100, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Signin.setFont(font)
        self.Signin.setObjectName("Signin")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(20, 80, 51, 16))
        self.user_label.setObjectName("user_label")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(20, 110, 51, 16))
        self.pass_label.setObjectName("pass_label")
        self.editUser = QtWidgets.QLineEdit(self.centralwidget)
        self.editUser.setGeometry(QtCore.QRect(80, 80, 161, 20))
        self.editUser.setObjectName("editUser")
        self.editPass = QtWidgets.QLineEdit(self.centralwidget)
        self.editPass.setGeometry(QtCore.QRect(80, 110, 161, 20))
        self.editPass.setObjectName("editPass")
        self.buttonLogin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLogin.setGeometry(QtCore.QRect(100, 140, 75, 23))
        self.buttonLogin.setObjectName("buttonLogin")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 170, 111, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 287, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttonLogin.clicked.connect(self.loginButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Experiment 4 Machine Problem 3"))
        self.Signin.setText(_translate("MainWindow", "Sign-In"))
        self.user_label.setText(_translate("MainWindow", "Username:"))
        self.pass_label.setText(_translate("MainWindow", "Password:"))
        self.buttonLogin.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Group Chat by Maui"))

    def loginButton(self):
        inUser = self.editUser.text()
        inPass = self.editPass.text()
        print(inUser)
        print(inPass)
        check = loginData(inUser, inPass)
        if check.MatchAcc() == True:
            self.openGC(inUser)
        else:
            self.label.setText('Invalid Login')

    def openGC(self, username):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ChatWindow()
        self.ui.setupUi(self.window,username)
        self.window.show()

class Ui_ChatWindow(object):
    def setupUi(self, MainWindow, username):
        self.chatCount = 0
        self.ChatEnable = True
        self.data = SharedCell()
        self.user = username

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 380, 291, 71))
        self.textEdit.setObjectName("textEdit")
        self.buttonSend = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSend.setGeometry(QtCore.QRect(314, 380, 51, 31))
        self.buttonSend.setObjectName("buttonSend")

        self.FormLayout = QFormLayout()
        self.GroupBox = QGroupBox(str('End of Conversation'))
        self.ServerSenderList = []
        self.ServerMsgList = []
        self.YouChatList = []
        self.YouPMList = []

        self.loadChat()
        self.GroupBox.setLayout(self.FormLayout)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(9, 40, 361, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = self.GroupBox
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")



        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 384, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttonSend.clicked.connect(self.addUserChatRow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(3000)

    def refresh(self):
        #for i in self.FormLayout.count():
        #    self.FormLayout.removeRow(i)
        print(self.chatCount)
        print(self.data.getMaxSheetIndex())
        self.data.refreshData()
        if (self.chatCount - 1) != self.data.getMaxSheetIndex():
            self.addServerChatRow()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatBot: EX4MP2"))
        self.Title.setText(_translate("MainWindow", "Group Chat"))
        self.buttonSend.setText(_translate("MainWindow", "Send"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>"))

    def loadChat(self):
        self.data.refreshData()
        for i, row in self.data.df.iterrows():
            self.ServerSenderList.append(QLabel(self.data.loadNameHead(i)))
            self.ServerMsgList.append(QLabel(self.data.loadMessage(i)))
            self.FormLayout.addRow(self.ServerSenderList[self.chatCount])
            self.FormLayout.addRow(self.ServerMsgList[self.chatCount])
            self.YouChatList.append(QLabel(''))
            self.YouPMList.append(QLabel(''))
            self.chatCount += 1

    def addUserChatRow(self):
        sentence = self.textEdit.toPlainText()
        self.YouChatList.append(QLabel('You ' + self.data.getDate() + ' ' + self.data.getTime()))
        self.YouPMList.append(QLabel(sentence))
        self.data.addMessage(self.user,sentence)
        self.FormLayout.addRow(self.YouChatList[self.chatCount])
        self.FormLayout.addRow(self.YouPMList[self.chatCount])
        self.ServerSenderList.append(QLabel(''))
        self.ServerMsgList.append(QLabel(''))
        self.GroupBox.setLayout(self.FormLayout)
        self.chatCount += 1

    def addServerChatRow(self):
        self.ServerSenderList.append(QLabel(self.data.loadNameHead(self.chatCount)))
        self.ServerMsgList.append(QLabel(self.data.loadMessage(self.chatCount)))
        self.FormLayout.addRow(self.ServerSenderList[self.chatCount])
        self.FormLayout.addRow(self.ServerMsgList[self.chatCount])
        self.YouChatList.append(QLabel(''))
        self.YouPMList.append(QLabel(''))
        self.GroupBox.setLayout(self.FormLayout)
        self.chatCount += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EX4MP2GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# Created by Marielle Gabriel


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QGroupBox, QPushButton, QFormLayout, QLabel, QWidget, QStackedWidget, QApplication
from PyQt5.QtGui import QIcon
from datetime import datetime
import random

class Doctor:
    hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.")
    qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")
    replacements = {"I": "you", "me": "you", "my": "your", "we": "you", "us": "you", "mine": "yours"}

    def reply(self, sentence):
        """Builds and returns a reply to the sentence."""
        probability = random.randint(1, 4)
        if probability == 1:
            return random.choice(self.hedges)
        else:
            return random.choice(self.qualifiers) + self.changePerson(sentence)

    def changePerson(self, sentence):
        """Replaces first person pronouns with second person pronouns."""
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(self.replacements.get(word, word))
        return " ".join(replyWords)

    def greeting(self, i):
        if i == 0:
            return str("Good morning, I hope you are well today.")
        elif i == 1:
            return str("If you would like to exit the conversation just type: QUIT")
        elif i == 2:
            return str("Please state your name.")

    def signoff(self):
        return str("Have a nice day!")

class TempData:
    def __init__(self):
        self.tempList = []

    def addtoList(self, string):
        self.tempList.append(string)

    def printList(self):
        print(self.tempList)

    def addData(self):
        with open("EX4MP2_data.txt", "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write(str(self.tempList))

    def readData(self):
        data = []
        with open("EX4MP2_data.txt", 'r') as file_object:
            file_contents = file_object.readlines()
            for line in file_contents:
                current_place = line[:-1]
                data.append(current_place)
        return file_contents

    def storeData(self, i):
        return self.readData()[i].strip('][').split(', ')

    def countLinesinData(self):
        with open("EX4MP2_data.txt") as f:
            for i, l in enumerate(f):
                pass
        return i + 1

class Ui_HistoryWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ctr = 0
        self.lineNum = 0
        self.lineCtr = 1

        self.Data_obj = TempData()
        self.FormLayout = QFormLayout()
        self.GroupBox = QGroupBox(str(datetime.now().strftime("%H:%M:%S")))
        self.DoctorChatList = []
        self.DoctorPmList = []
        self.YouChatList = []
        self.YouPMList = []

        self.loadChat()
        #print(self.Data_obj.countLinesinData())

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 311, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = self.GroupBox
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.button_next = QtWidgets.QPushButton(self.centralwidget)
        self.button_next.setGeometry(QtCore.QRect(240, 350, 75, 23))
        self.button_next.setObjectName("button_next")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 350, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.button_next.clicked.connect(self.nextPress)
        self.pushButton_2.clicked.connect(self.prevPress)



        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat History"))
        self.button_next.setText(_translate("MainWindow", "Next"))
        self.pushButton_2.setText(_translate("MainWindow", "Previous"))

    def nextPress(self):
        self.ctr = 0
        self.lineNum += 1
        print(self.lineCtr)
        print(self.Data_obj.countLinesinData())
        if self.lineCtr < self.Data_obj.countLinesinData():
            self.loadChat()
            self.lineCtr += 1

    def prevPress(self):
        self.ctr = 0
        self.lineNum -= 1
        if self.lineCtr > 0:
            self.loadChat()
            self.lineCtr -= 1

    def loadChat(self):
        histList = self.Data_obj.storeData(self.lineNum)
        for i in range(0, 3):
            self.DoctorChatList.append(QLabel('Doctor'))
            self.DoctorPmList.append(QLabel(histList[self.ctr][1:-1]))
            self.YouChatList.append(QLabel(''))
            self.YouPMList.append(QLabel(''))
            self.FormLayout.addRow(self.DoctorChatList[self.ctr])
            self.FormLayout.addRow(self.DoctorPmList[self.ctr])
            self.ctr += 1

        while self.ctr < len(histList):
            if (self.ctr % 2) != 0:
                self.DoctorChatList.append(QLabel('Doctor'))
                self.DoctorPmList.append(QLabel(histList[self.ctr][1:-1]))
                self.FormLayout.addRow(self.DoctorChatList[self.ctr])
                self.FormLayout.addRow(self.DoctorPmList[self.ctr])
            else:
                self.DoctorPmList.append(QLabel(''))
                self.DoctorChatList.append(QLabel(''))
            if (self.ctr % 2) == 0:
                self.YouChatList.append(QLabel('You'))
                self.YouPMList.append(QLabel(histList[self.ctr][1:-1]))
                self.FormLayout.addRow(self.YouChatList[self.ctr])
                self.FormLayout.addRow(self.YouPMList[self.ctr])
            else:
                self.YouChatList.append(QLabel(''))
                self.YouPMList.append(QLabel(''))
            self.ctr += 1
        self.GroupBox.setLayout(self.FormLayout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.chatCount = 0
        self.ChatEnable = True
        self.data = TempData()

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
        self.buttonHistory = QtWidgets.QPushButton(self.centralwidget)
        self.buttonHistory.setGeometry(QtCore.QRect(280, 10, 91, 23))
        self.buttonHistory.setObjectName("buttonHistory")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 380, 291, 71))
        self.textEdit.setObjectName("textEdit")
        self.buttonSend = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSend.setGeometry(QtCore.QRect(314, 380, 51, 31))
        self.buttonSend.setObjectName("buttonSend")

        self.Doc = Doctor()

        self.FormLayout = QFormLayout()
        self.GroupBox = QGroupBox(str(datetime.now().strftime("%H:%M:%S")))
        self.DoctorChatList = []
        self.DoctorPmList = []
        self.YouChatList = []
        self.YouPMList = []
        for i in range(0, 3):
            self.DoctorChatList.append(QLabel('Doctor ' + str(datetime.now().strftime("%H:%M:%S"))))
            self.DoctorPmList.append(QLabel(self.Doc.greeting(i)))
            self.data.addtoList(self.Doc.greeting(i))
            self.YouChatList.append(QLabel(''))
            self.YouPMList.append(QLabel(''))
            self.FormLayout.addRow(self.DoctorChatList[self.chatCount])
            self.FormLayout.addRow(self.DoctorPmList[self.chatCount])
            self.chatCount += 1
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

        if self.ChatEnable == True:
            self.buttonSend.clicked.connect(self.addChatRow)
        self.buttonHistory.clicked.connect(self.openHistory)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatBot: EX4MP2"))
        self.Title.setText(_translate("MainWindow", "Doctor BotBot"))
        self.buttonHistory.setText(_translate("MainWindow", "History"))
        self.buttonSend.setText(_translate("MainWindow", "Send"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>"))
        #self.chatDoctor.setText(_translate("MainWindow", "Doctor BotBot"))
        #self.chatMessage.setText(_translate("MainWindow", "TextLabel"))
        #self.chatYou.setText(_translate("MainWindow", "You"))
        #self.chatSent.setText(_translate("MainWindow", "TextLabel"))

    def addChatRow(self):
        sentence = self.textEdit.toPlainText()
        self.YouChatList.append(QLabel('You ' + str(datetime.now().strftime("%H:%M:%S"))))
        self.YouPMList.append(QLabel(sentence))
        self.data.addtoList(sentence)
        self.FormLayout.addRow(self.YouChatList[self.chatCount])
        self.FormLayout.addRow(self.YouPMList[self.chatCount])
        if sentence.upper() == 'QUIT':
            self.DoctorChatList.append(QLabel('Doctor ' + str(datetime.now().strftime("%H:%M:%S"))))
            self.DoctorPmList.append(QLabel(self.Doc.signoff()))
            self.data.addtoList(str(self.Doc.signoff()))
            self.FormLayout.addRow(self.DoctorChatList[self.chatCount])
            self.FormLayout.addRow(self.DoctorPmList[self.chatCount])
            self.data.addData()
        else:
            self.DoctorChatList.append(QLabel('Doctor ' + str(datetime.now().strftime("%H:%M:%S"))))
            self.DoctorPmList.append(QLabel(self.Doc.reply(sentence)))
            self.data.addtoList(self.Doc.reply(sentence))
            self.FormLayout.addRow(self.DoctorChatList[self.chatCount])
            self.FormLayout.addRow(self.DoctorPmList[self.chatCount])
            self.GroupBox.setLayout(self.FormLayout)
            self.chatCount += 1

    def openHistory(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HistoryWindow()
        self.ui.setupUi(self.window)
        self.window.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

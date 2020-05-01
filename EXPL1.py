# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EX4PL1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Temperature:
    def __init__(self):
        self.Fahreinheit = 32
        self.Celsius = 0

    def setFahr(self, F):
        self.Fahreinheit = F
        self.Celsius = self.getCels()

    def setCels(self, C):
        self.Celsius = C
        self.Fahreinheit = self.getFahr()

    def getFahr(self):
        return round((self.Celsius * (9/5)) + 32, 2)

    def getCels(self):
        return round((self.Fahreinheit - 32) * (5/9), 2)


class Ui_MainWindow(object):
    conv = Temperature()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 208)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonFahr = QtWidgets.QPushButton(self.centralwidget)
        self.buttonFahr.setGeometry(QtCore.QRect(20, 110, 75, 23))
        self.buttonFahr.setObjectName("buttonFahr")
        self.puttonCel = QtWidgets.QPushButton(self.centralwidget)
        self.puttonCel.setGeometry(QtCore.QRect(240, 110, 75, 23))
        self.puttonCel.setObjectName("puttonCel")
        self.Header = QtWidgets.QLabel(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(20, 40, 121, 16))
        self.Header.setTextFormat(QtCore.Qt.AutoText)
        self.Header.setObjectName("Header")
        self.FahrEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.FahrEdit.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.FahrEdit.setObjectName("FahrEdit")
        self.CelsEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.CelsEdit.setGeometry(QtCore.QRect(240, 80, 113, 20))
        self.CelsEdit.setObjectName("CelsEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.puttonCel.clicked.connect(self.setValFar)
        self.buttonFahr.clicked.connect(self.setValCel)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Temperature Converter Experiment 4 Post Lab MP 1"))
        self.buttonFahr.setText(_translate("MainWindow", ">>>>"))
        self.puttonCel.setText(_translate("MainWindow", "<<<<"))
        self.Header.setText(_translate("MainWindow", "Temperature Converter"))
        self.FahrEdit.setText(_translate("MainWindow", "32.0°F"))
        self.CelsEdit.setText(_translate("MainWindow", "0°C"))

    def printVal(self):
        self.FahrEdit.setText(str(str(self.conv.getFahr()) + "°F"))
        self.CelsEdit.setText(str(str(self.conv.getCels()) + "°C"))

    def setValFar(self):
        try:
            self.conv.setCels(float(self.CelsEdit.text()))
        except ValueError:
            try:
                self.conv.setCels(float(self.CelsEdit.text()[:-2]))
            except ValueError:
                self.CelsEdit.setText("Invalid Input")
        else:
            self.printVal()

    def setValCel(self):
        try:
            self.conv.setFahr(float(self.FahrEdit.text()))
        except ValueError:
            try:
                self.conv.setFahr(float(self.FahrEdit.text()[:-2]))
            except ValueError:
                self.FahrEdit.setText("Invalid Input")
        else:
            self.printVal()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

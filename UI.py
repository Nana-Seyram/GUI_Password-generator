from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random
import string 
import pyperclip


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(-10, -40, 631, 511))
        self.Background.setAutoFillBackground(False)
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("BingWallpaper (3).jpg"))
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        self.Generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.Generate_button.setGeometry(QtCore.QRect(170, 50, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Generate_button.setFont(font)
        self.Generate_button.setObjectName("Generate_button")
        self.Display = QtWidgets.QLabel(self.centralwidget)
        self.Display.setGeometry(QtCore.QRect(80, 170, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Display.setFont(font)
        self.Display.setAutoFillBackground(False)
        self.Display.setObjectName("Display")
        self.Copy_button = QtWidgets.QPushButton(self.centralwidget)
        self.Copy_button.setGeometry(QtCore.QRect(164, 280, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Copy_button.setFont(font)
        self.Copy_button.setObjectName("Copy_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Mapping funcions to buttons
        self.Generate_button.clicked.connect(self.gen_password)
        self.Copy_button.clicked.connect(self.copy_password)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Generate_button.setText(_translate("MainWindow", "Generate Password"))
        self.Display.setText(_translate("MainWindow", "TextLabel"))
        self.Copy_button.setText(_translate("MainWindow", "Copy"))

    #This function generates a password
    def gen_password(self):
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = lowercase.upper()
        num = str(range(13,23))
        sym = string.punctuation

        all = uppercase + lowercase + num + sym

        self.password = "".join(random.sample(all, 12))

        self.Display.setText(f"password: {self.password}")
        self.Display.adjustSize()

    #This function copies the password to clipboard
    def copy_password(self):
        pyperclip.copy(self.password)
        msg = QMessageBox()
        msg.setWindowTitle("Sucessful")
        msg.setText("Copied")

        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

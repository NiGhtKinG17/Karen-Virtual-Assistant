# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'karenUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KarenUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1256, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 1271, 811))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("mainbg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(228, 115, 800, 600))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("run.gif"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(4, 5, 381, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("tl.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(563, 395, 130, 40))
        self.pushButton.setStyleSheet("font-size:20px;\n"
"background-color: rgb(0, 255, 255);\n"
"font: 20pt \"Stencil\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(900, 510, 361, 281))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("plexus___3.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 30, 91, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 16pt \"Stencil\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 650, 381, 101))
        self.label_5.setStyleSheet("color: rgb(0, 255, 255);\n"
"font: 48pt \"Stencil\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 190, 291, 71))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("frame.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 270, 291, 71))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("frame.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 200, 231, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 18pt \"Stencil\";\n"
"color: rgb(0, 255, 255);\n"
"padding-left:33px;\n"
"padding-top:3px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(80, 280, 231, 51))
        self.textBrowser_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 18pt \"Stencil\";\n"
"color: rgb(0, 255, 255);\n"
"padding-left:50px;\n"
"padding-top:3px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1256, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "RUN"))
        self.pushButton_2.setText(_translate("MainWindow", "EXIT"))
        self.label_5.setText(_translate("MainWindow", "K A R E N"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_KarenUi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

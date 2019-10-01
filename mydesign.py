# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 650)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(40, 40, 1211, 571))
        self.listWidget.setStyleSheet("\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(517, 290, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 70, 571, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 420, 170, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 373, 291, 25))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(552, 533, 181, 25))
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(528, 320, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(1010, 50, 231, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo1.jpg"))
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(1090, 160, 81, 25))
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Arhillect"))
        self.lineEdit.setText(_translate("Form", "Добро пожаловать"))
        self.pushButton.setText(_translate("Form", "Начать"))
        self.lineEdit_2.setText(_translate("Form", "Психоэмоциональный тренажер ver 1.01"))
        self.lineEdit_3.setText(_translate("Form", "Design by Arhillect 2019"))
        self.lineEdit_6.setText(_translate("Form", "Марша дог1ийла"))
        self.lineEdit_4.setText(_translate("Form", "ГРОЗНЫЙ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

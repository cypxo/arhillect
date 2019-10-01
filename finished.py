# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finished.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class finished(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(652, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(-10, 0, 671, 971))
        self.listView.setAutoScroll(False)
        self.listView.setObjectName("listView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 480, 731, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 400, 145, 61))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 50, 151, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("train/like.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 531, 131))
        self.label_3.setObjectName("label_3")
        self.listView.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тренировка"))
        self.label.setText(_translate("MainWindow", "FINISHED"))
        self.pushButton.setText(_translate("MainWindow", "Начать заново"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Liberation Serif,serif\'; font-size:14pt; font-weight:600; background-color:transparent;\">Вы прошли все упражнения! Молодцы!</span></p><p><span style=\" font-family:\'Liberation Serif,serif\'; font-size:14pt; font-weight:600; background-color:transparent;\">Заходите и тренируйте свои эмоции почаще,</span></p><p><span style=\" font-family:\'Liberation Serif,serif\'; font-size:14pt; font-weight:600; background-color:transparent;\">для более быстрой восстановления мимики, или нажмите</span></p><p><span style=\" font-family:\'Liberation Serif,serif\'; font-size:14pt; font-weight:600; background-color:transparent;\">на кнопку &quot;Начать заново&quot;.</span></p><p><span style=\" font-family:\'Liberation Serif,serif\'; font-size:14pt; font-weight:600; background-color:transparent;\">Удачи!</span></p><p><br/></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = finished()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

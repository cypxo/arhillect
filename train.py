# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class train(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(650, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 6, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(-10, 0, 661, 971))
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 105, 17))
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 120, 646, 226))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("train/zaborchik.jpeg"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 400, 155, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 601, 61))
        self.label_5.setObjectName("label_5")
        self.listView.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.pushButton_2.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тренировка"))
        self.label.setText(_translate("MainWindow", "Упражнения"))
        self.pushButton.setText(_translate("MainWindow", "Начать тренировку"))
        self.label_3.setText(_translate("MainWindow", "Задание 1."))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><h3 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:transparent;\"><span style=\" font-family:\'Liberation Serif,serif\'; font-size:14pt; font-weight:600; background-color:transparent;\">«</span>ЗАБОРЧИК»</h3><p>• исходное положение. Рот закрыт, </p><p>зубы сомкнуты. </p><p>• растягиваю губы в улыбке. Так что бы</p><p>верхние и нижние зубы были обнажены. </p><p>• удерживаю растянутую улыбку 2 сек. </p><p>• возвращаюсь в исходное положение на 2 сек. </p><p>• 8 повторений х 1 подход. </p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Следующее задание"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Всего упражнений 7. На выполнение заданий, время, дается смотря насколько</p><p>сложное задание. Следующее задание будет доступно после выполние нынешной</p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = train()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

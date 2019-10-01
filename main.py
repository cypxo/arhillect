import sys
from PyQt5 import QtWidgets, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QProgressBar
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)
from PyQt5.QtCore import QBasicTimer
from mydesign import Ui_Form
from train import train
from train2 import train2
from train3 import train3
from train4 import train4
from train5 import train5
from train6 import train6
from train7 import train7
from finished import finished

class window_8(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setGeometry(1750, 1750,0,0)
        self.ui = finished()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Open_w8)
    def Open_w8(self):
        self.WindowShow = Window()
        self.WindowShow.show()
        self.close()

class window_7(QtWidgets.QMainWindow, train7):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setGeometry(1750, 1750,0,0)
        self.ui = train7()
        self.ui.setupUi(self)
        self.pbar = QProgressBar(self)
        self.ui.pushButton.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0   
        self.pbar.setGeometry(10, 375, 630, 20)
        self.ui.pushButton_2.clicked.connect(self.Open_w8)

        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.ui.pushButton.setText('Отлично!')
            self.ui.pushButton_2.setEnabled(True)
            return
            
        self.step = self.step + 0.1
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.ui.pushButton.setText('Продолжить')
        else:
            self.timer.start(100, self)
            self.ui.pushButton.setText('Стоп')
    def Open_w8(self):
        self.WindowShow = window_8()
        self.WindowShow.show()
        self.close()

class window_6(QtWidgets.QMainWindow, train6):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setGeometry(1750, 1750,0,0)
        self.ui = train6()
        self.ui.setupUi(self)
        self.pbar = QProgressBar(self)
        self.ui.pushButton.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0   
        self.pbar.setGeometry(10, 375, 630, 20)
        self.ui.pushButton_2.clicked.connect(self.Open_w7)

        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.ui.pushButton.setText('Отлично!')
            self.ui.pushButton_2.setEnabled(True)
            return
            
        self.step = self.step + 0.60
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.ui.pushButton.setText('Продолжить')
        else:
            self.timer.start(100, self)
            self.ui.pushButton.setText('Стоп')
    def Open_w7(self):
        self.WindowShow = window_7()
        self.WindowShow.show()
        self.close()

class window_5(QtWidgets.QMainWindow, train5):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setGeometry(1750, 1750,0,0)
        self.ui = train5()
        self.ui.setupUi(self)
        self.pbar = QProgressBar(self)
        self.ui.pushButton.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0   
        self.pbar.setGeometry(10, 375, 630, 20)
        self.ui.pushButton_2.clicked.connect(self.Open_w6)

        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.ui.pushButton.setText('Отлично!')
            self.ui.pushButton_2.setEnabled(True)
            return
            
        self.step = self.step + 0.4
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.ui.pushButton.setText('Продолжить')
        else:
            self.timer.start(100, self)
            self.ui.pushButton.setText('Стоп')
    def Open_w6(self):
        self.WindowShow = window_6()
        self.WindowShow.show()
        self.close()

class window_4(QtWidgets.QMainWindow, train4):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setGeometry(1750, 1750,0,0)
        self.ui = train4()
        self.ui.setupUi(self)
        self.pbar = QProgressBar(self)
        self.ui.pushButton.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0   
        self.pbar.setGeometry(10, 375, 630, 20)
        self.ui.pushButton_2.clicked.connect(self.Open_w5)

        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.ui.pushButton.setText('Отлично!')
            self.ui.pushButton_2.setEnabled(True)
            return
            
        self.step = self.step + 0.10
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.ui.pushButton.setText('Продолжить')
        else:
            self.timer.start(100, self)
            self.ui.pushButton.setText('Стоп')
    def Open_w5(self):
        self.WindowShow = window_5()
        self.WindowShow.show()
        self.close()

class window_3(QtWidgets.QMainWindow, train3):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setGeometry(1750, 1750,0,0)
        self.ui = train3()
        self.ui.setupUi(self)
        self.pbar = QProgressBar(self)
        self.ui.pushButton.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0   
        self.pbar.setGeometry(10, 375, 630, 20)
        self.ui.pushButton_2.clicked.connect(self.Open_w4)

        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.ui.pushButton.setText('Отлично!')
            self.ui.pushButton_2.setEnabled(True)
            return
            
        self.step = self.step + 0.5
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.ui.pushButton.setText('Продолжить')
        else:
            self.timer.start(100, self)
            self.ui.pushButton.setText('Стоп')
    def Open_w4(self):
        self.WindowShow = window_4()
        self.WindowShow.show()
        self.close()

class window_2(QtWidgets.QMainWindow, train2):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setGeometry(1750, 1750,0,0)
        self.ui = train2()
        self.ui.setupUi(self)
        self.pbar = QProgressBar(self)
        self.ui.pushButton.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0   
        self.pbar.setGeometry(10, 375, 630, 20)
        self.ui.pushButton_2.clicked.connect(self.Open_w3)

        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.ui.pushButton.setText('Отлично!')
            self.ui.pushButton_2.setEnabled(True)
            return
            
        self.step = self.step + 0.11
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.ui.pushButton.setText('Продолжить')
        else:
            self.timer.start(100, self)
            self.ui.pushButton.setText('Стоп')
    def Open_w3(self):
        self.WindowShow = window_3()
        self.WindowShow.show()
        self.close()

class Window(QtWidgets.QMainWindow, train):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setGeometry(1750, 1750,0,0)
        self.ui = train()
        self.ui.setupUi(self)
        self.pbar = QProgressBar(self)
        self.ui.pushButton.clicked.connect(self.doAction)
 
        self.timer = QBasicTimer()
        self.step = 0
        
        self.pbar.setGeometry(10, 375, 630, 20)
        self.ui.pushButton_2.clicked.connect(self.Open_w2)

        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.ui.pushButton.setText('Отлично!')
            self.ui.pushButton_2.setEnabled(True)
            return
            
        self.step = self.step + 0.33
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.ui.pushButton.setText('Продолжить')
        else:
            self.timer.start(100, self)
            self.ui.pushButton.setText('Стоп')
    def Open_w2(self):
        self.WindowShow = window_2()
        self.WindowShow.show()
        self.close()
            
class mywindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Open)
        
    def Open(self):
        self.WindowShow = Window()
        self.WindowShow.show()
        import run

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()
sys.exit(app.exec())

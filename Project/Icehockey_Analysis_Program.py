import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip, QGridLayout, 
QLineEdit, QInputDialog)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QCoreApplication
import threading
import time


class MyApp(QWidget) :
    
    def __init__(self) :
        super().__init__()
        self.initUI()
        
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout)
        
        self.setWindowTitle('DataAnalysis')
        self.setGeometry(100, 100, 600, 800)
        
        layout = QVBoxLayout()

        self.lcd = QLCDNumber()
        self.lcd.display('')
        self.lcd.setDigitCount(8)
        
        subLayout = QHBoxLayout()
        
        layout.addWidget(self.lcd)
        
    def timeout(self) :
        sender = self.sender()
        currentTime = QTime.currentTime().toString('hh:mm:ss')
        
        if id (sender) == id(self.timer) :
            self.lcd.display(currentTime)

    def initUI(self) :
        grid = QGridLayout()
        self.setLayout(grid)
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('시작 \n (space)', self)
        btn.setToolTip('This is a start widget')
        btn.move(220, 50)
        btn.resize(150, 45)
        
        self.btn = QPushButton('시간변경', self)
        self.btn.setToolTip('This is a change time widget')
        self.btn.move(220, 130)
        self.btn.resize(150, 45)
        self.btn.clicked.connect(self.showDialog)
        
        self.setWindowTitle('IceHockey')
        self.setWindowIcon(QIcon('hockey_icon.png'))
        self.setGeometry(0, 0, 1800, 1000)

        image_path = 'ice_rink.png'

        pixmap = QPixmap(image_path)
        label = QLabel()
        label.setPixmap(pixmap)
        grid.addWidget(label)

        self.setLayout(grid)
        label.move(100, 100)

        self.setWindowTitle('Image Display')
        self.setGeometry(1000, 800, 800, 800)

        self.show()
        
    def timeout(self):
        sender = self.sender()
        
    def showDialog(self) :
        text, ok = QInputDialog.getText(self, '시간 변경', '시간 변경 (mm : ss)')

        if ok:
            self.le.setText(str(text))

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
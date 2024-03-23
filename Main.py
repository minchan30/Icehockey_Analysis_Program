import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QLCDNumber, QInputDialog, QMainWindow
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter, QPen
from PyQt5.QtCore import QTimer, QTime, Qt

from model.Timer import Timer

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.asset_path = self.base_path + "\\assets"
        self.model_path = self.base_path + "\\model"

        self.initUI()

    def initUI(self):
        self.setWindowTitle('IceHockey')
        self.setWindowIcon(QIcon(self.asset_path + '\\ico_hockey.png'))
        
        self.vbox = QVBoxLayout()
        self.inner_hbox = QHBoxLayout()
        self.inner_hbox.addLayout(Timer(self, self.base_path))
        self.inner_hbox.addLayout(Timer(self, self.base_path))
        self.vbox.addLayout(self.inner_hbox)
        
        self.setLayout(self.vbox)
        
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
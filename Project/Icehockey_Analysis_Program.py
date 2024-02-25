import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip, QGridLayout, 
                             QHBoxLayout, QVBoxLayout, QLabel, QLCDNumber, QInputDialog)
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter, QPen
from PyQt5.QtCore import QTimer, QTime, Qt

class MyApp(QWidget):    

    def __init__(self):
        super().__init__()
        self.initUI()
       
    def initUI(self):
        self.setWindowTitle('IceHockey')
        self.setWindowIcon(QIcon('hockey_icon.png'))
        
        black_box = QLabel(self)
        black_box_pixmap = QPixmap('black.png')
        black_box_pixmap = black_box_pixmap.scaled(300, 370)
        black_box.setPixmap(black_box_pixmap)
        
        btn_start = QPushButton('시작 \n (space)', self)
        btn_start.setFixedSize(230, 70)
        btn_start.setToolTip('This is a start widget')
        
        btn_change_time = QPushButton('시간변경', self)
        btn_change_time.setToolTip('This is a change time widget')
        
        inner_vbox = QVBoxLayout()
        inner_vbox.addWidget(btn_start)
        inner_vbox.addWidget(btn_change_time)

        black_box2 = QLabel(self)
        black_box_pixmap2 = QPixmap('black.png')
        black_box_pixmap2 = black_box_pixmap2.scaled(300, 320)
        black_box2.setPixmap(black_box_pixmap2)

        inner_vbox2 = QVBoxLayout()
        inner_vbox2.addStretch(1)
        inner_vbox2.addWidget(black_box2)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(black_box)
        hbox.addLayout(inner_vbox)
        hbox.addLayout(inner_vbox2)
        hbox.addStretch(100)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        ice_rink = QLabel(self)
        ice_rink = QPixmap('ice_rink.png')
        ice_rink_pixmap = ice_rink_pixmap.scaled(300, 370)
        ice_rink.setPixmap(ice_rink)

        inner_vbox3 = QVBoxLayout()
        inner_vbox3.addStretch(1)
        inner_vbox.addWidget(ice_rink)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(black_box)
        hbox.addLayout(inner_vbox)
        hbox.addLayout(inner_vbox2)
        hbox.addStretch(100)



        self.setLayout(vbox)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
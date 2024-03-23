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

        ice_rink = QLabel(self)
        ice_rink_pixmap = QPixmap('ice_rink.png')
        ice_rink_pixmap = ice_rink_pixmap.scaled(1400, 700)
        ice_rink.setPixmap(ice_rink_pixmap)
        
        black_box = QLabel(self)
        black_box_pixmap = QPixmap('black.png')
        black_box_pixmap = black_box_pixmap.scaled(300, 370)
        black_box.setPixmap(black_box_pixmap)

        black_box2 = QLabel(self)
        black_box_pixmap2 = QPixmap('black.png')
        black_box_pixmap2 = black_box_pixmap2.scaled(300, 320)
        black_box2.setPixmap(black_box_pixmap2)
        
        btn_start = QPushButton('시작 \n (space)', self)
        btn_start.setFixedSize(290, 75)
        btn_start.setToolTip('This is a start widget')
        
        btn_change_time = QPushButton('시간변경', self)
        btn_change_time.setFixedSize(290, 35)
        btn_change_time.setToolTip('This is a change time widget')

        btn_home_plus = QPushButton('홈 스코어 증가 \n +', self)
        btn_home_plus.setFixedSize(290, 75)
        btn_home_plus.setToolTip('This is a home score plus widget')

        btn_home_minus = QPushButton('홈 스코어 감소 \n -', self)
        btn_home_minus.setFixedSize(290, 75)
        btn_home_minus.setToolTip('This is a home score minus widget')

        btn_away_plus = QPushButton('어웨이 스코어 증가 \n +', self)
        btn_away_plus.setFixedSize(290, 75)
        btn_away_plus.setToolTip('This is a away score plus widget')

        btn_away_minus = QPushButton('어웨이 스코어 감소 \n -', self)
        btn_away_minus.setFixedSize(290, 75)
        btn_away_minus.setToolTip('This is a away score minus widget')

##________________________________________홈_________________________________________________
        btn_home_shoot = QPushButton('홈 슛 버튼 \n (Q)', self)
        btn_home_shoot.setFixedSize(320, 75)

        btn_home_shoot = QPushButton('홈 패스 버튼 \n (W)', self)
        btn_home_shoot.setFixedSize(320, 75)

        btn_home_shoot = QPushButton('홈 체킹 버튼 \n (E)', self)
        btn_home_shoot.setFixedSize(320, 75)

        btn_home_shoot = QPushButton('홈 턴오버 버튼 \n (R)', self)
        btn_home_shoot.setFixedSize(320, 75)

        btn_home_shoot = QPushButton('홈 패스/리시브미스 버튼 \n (T)', self)
        btn_home_shoot.setFixedSize(320, 75)

#______________________________________어웨이 _______________________________________________
        btn_home_shoot = QPushButton('홈 골 버튼 \n (Y)', self)
        btn_home_shoot.setFixedSize(320, 75)

        btn_home_shoot = QPushButton('어웨이 슛 버튼 \n (A)', self)
        btn_home_shoot.setFixedSize(320, 75)

        btn_home_shoot = QPushButton('어웨이 패스 버튼 \n (S)', self)
        btn_home_shoot.setFixedSize(320, 75)

        btn_home_shoot = QPushButton('어웨이 체킹 버튼 \n (D)', self)
        btn_home_shoot.setFixedSize(320, 75)

        btn_home_shoot = QPushButton('어웨이 턴오버 버튼 \n (F)', self)
        btn_home_shoot.setFixedSize(320, 75)

        btn_home_shoot = QPushButton('어웨이 패스/리시브미스 버튼 \n (G)', self)
        btn_home_shoot.setFixedSize(320, 75)

        btn_home_shoot = QPushButton('어웨이 골 버튼 \n (H)', self)
        btn_home_shoot.setFixedSize(320, 75)

#______________________________________________________________________________________________________________________________________________________________
        # 1-2번째
        inner_vbox = QVBoxLayout()
        inner_vbox.addWidget(btn_start)
        inner_vbox.addWidget(btn_change_time)

        inner_vbox2 = QVBoxLayout()
        inner_vbox2.addStretch(1)
        inner_vbox2.addWidget(black_box2)

        inner_vbox3 = QVBoxLayout()
        inner_vbox3.addWidget(btn_home_plus)
        inner_vbox3.addWidget(btn_home_minus)

        inner_vbox4 = QVBoxLayout()
        inner_vbox4.addWidget(btn_away_plus)
        inner_vbox4.addWidget(btn_away_minus)

        hbox = QHBoxLayout()
        hbox.addStretch(30)
        hbox.addWidget(black_box)
        hbox.addStretch(30)
        hbox.addLayout(inner_vbox)
        hbox.addStretch(30)
        hbox.addLayout(inner_vbox2)
        hbox.addStretch(30)
        hbox.addLayout(inner_vbox3)
        hbox.addStretch(30)
        hbox.addLayout(inner_vbox4)
        hbox.addStretch(1000)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        hbox.addStretch(30)
        vbox.addWidget(ice_rink)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
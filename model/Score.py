from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect

class Score(QHBoxLayout) :
    def __init__(self, widget, base_path) :
        super().__init__()
        self.black_box = QLabel(widget)
        self.black_box_pixmap = QPixmap(base_path + '\\assets\\bg_black.png')
        self.black_box_pixmap = self.black_box_pixmap.scaled(300, 320)
        self.black_box.setPixmap(self.black_box_pixmap)

        self.home_plus_btn = QPushButton('홈 스코어 증가 \n +', widget)
        self.home_minus_btn = QPushButton('홈 스코어 감소 \n -', widget)
        self.away_plus_btn = QPushButton('어웨이 스코어 증가 \n +', widget)
        self.away_minus_btn = QPushButton('어웨이 스코어 감소 \n -', widget)

         # 수평 레이아웃 생성하고 버튼 추가
        hbox_home_score = QHBoxLayout()
        hbox_home_score.addWidget(self.home_plus_btn)
        hbox_home_score.addWidget(self.home_minus_btn)

         # 수평 레이아웃 생성하고 버튼 추가
        hbox_away_score = QHBoxLayout()
        hbox_away_score.addWidget(self.away_plus_btn)
        hbox_away_score.addWidget(self.away_minus_btn)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(hbox_home_score)
        self.vbox.addLayout(hbox_away_score)
        

        self.addWidget(self.black_box)
        self.addLayout(self.vbox)

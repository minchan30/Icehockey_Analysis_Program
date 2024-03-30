from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect

class Timer(QHBoxLayout) :
    def __init__(self, widget, base_path) :
        super().__init__()
        self.black_box = QLabel(widget)
        self.black_box_pixmap = QPixmap(base_path + '\\assets\\bg_black.png')
        self.black_box_pixmap = self.black_box_pixmap.scaled(300, 370)
        self.black_box.setPixmap(self.black_box_pixmap)
       
        self.start_btn = QPushButton('시작 \n (start)', widget)
        self.change_time_btn = QPushButton('시간변경', widget)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.start_btn)
        self.vbox.addWidget(self.change_time_btn)

        self.addWidget(self.black_box)
        self.addLayout(self.vbox)

        

        

        
        
        

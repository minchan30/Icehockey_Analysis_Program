from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect

class Timer(QHBoxLayout) :
    def __init__(self, widget, base_path) :
        super().__init__()
        self.black_box = QLabel(widget)
        self.black_box_pixmap = QPixmap(base_path + '\\assets\\bg_black.png')

        self.remove_btn = QPushButton('삭제', widget)

        self.black_box_pixmap = self.black_box_pixmap.scaled(130, 180)
        self.black_box.setPixmap(self.black_box_pixmap)
        
        hbox_remove = QHBoxLayout()
        hbox_remove.addWidget(self.remove_btn)
        hbox_remove.addWidget(self.remove_btn)
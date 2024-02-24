import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip, QGridLayout, 
                             QHBoxLayout, QVBoxLayout, QLabel, QLCDNumber, QInputDialog)
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter, QPen
from PyQt5.QtCore import QTimer, QTime, Qt

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # 타이머 생성 및 설정
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # 1초마다 timeout 시그널 발생
        self.timer.timeout.connect(self.timeout)  # timeout 시그널이 발생할 때 호출할 함수 설정
        
        self.setWindowTitle('DataAnalysis')
        self.setGeometry(100, 100, 600, 800)
        
        layout = QVBoxLayout()
        self.lcd = QLCDNumber()  # 시간을 표시할 LCD 위젯 생성
        self.lcd.display('')  # 초기 표시 내용 설정
        self.lcd.setDigitCount(8)  # 디스플레이되는 숫자 자릿수 설정
        layout.addWidget(self.lcd)  # LCD 위젯을 레이아웃에 추가
        
    def timeout(self):
        currentTime = QTime.currentTime().toString('hh:mm:ss')
        self.lcd.display(currentTime)  # LCD에 현재 시간 표시

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        QToolTip.setFont(QFont('SansSerif', 10))
        
        btn = QPushButton('시작 \n (space)', self)  # 시작 버튼 생성
        btn.setToolTip('This is a start widget')
        btn.move(360, 70)
        btn.resize(280, 70)
        
        self.btn = QPushButton('시간변경', self)  # 시간 변경 버튼 생성
        self.btn.setToolTip('This is a change time widget')
        self.btn.move(360, 190)
        self.btn.resize(280, 70)
        self.btn.clicked.connect(self.showDialog)  # 버튼 클릭 시 showDialog() 메서드 호출
        
        self.setWindowTitle('IceHockey')
        self.setWindowIcon(QIcon('hockey_icon.png'))  # 창 아이콘 설정
        self.setGeometry(0, 0, 1800, 1000)

        label = QLabel(self)
        pixmap = QPixmap('ice_rink.png')
        pixmap = pixmap.scaled(1250, 625)
        label.setPixmap(pixmap)
        label.move(30, 190)
        label.setFixedSize(1000, 1000)

        self.show()
        
    def showDialog(self):
        text, ok = QInputDialog.getText(self, '시간 변경', '시간 변경 (mm:ss)')  # 다이얼로그 표시

        if ok:
            self.lcd.display(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
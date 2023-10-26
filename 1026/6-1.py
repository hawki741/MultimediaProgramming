from PyQt5.QtWidgets import *       # PyQt5 설치
import sys
import winsound

class BeepSound(QMainWindow):
    def __init__(self) :                        # 초기 윈도우에 대한 설정
        super().__init__()
        self.setWindowTitle('삑 소리 내기') 		# 윈도우 이름과 위치 지정
        self.setGeometry(200,200,500,100)       # 윈도우의 위치 : 모니터 좌상단을 기준으로 (x,y,w,h)

        shortBeepButton=QPushButton('짧게 삑',self)	# 버튼 생성
        longBeepButton=QPushButton('길게 삑',self)
        quitButton=QPushButton('나가기',self)
        self.label=QLabel('환영합니다!',self)
        
        shortBeepButton.setGeometry(10,10,100,30)	# 버튼 위치와 크기 지정 : 윈도우 좌상단을 기준으로 (x,y,w,h)
        longBeepButton.setGeometry(110,10,100,30)
        quitButton.setGeometry(210,10,100,30)
        self.label.setGeometry(10,40,500,70)
        
        shortBeepButton.clicked.connect(self.shortBeepFunction) # 콜백 함수 지정
        longBeepButton.clicked.connect(self.longBeepFunction)         
        quitButton.clicked.connect(self.quitFunction)
       
    def shortBeepFunction(self):
        self.label.setText('주파수 1000으로 0.5초 동안 삑 소리를 냅니다.')   
        winsound.Beep(1000,500)
        
    def longBeepFunction(self):
        self.label.setText('주파수 1000으로 3초 동안 삑 소리를 냅니다.')        
        winsound.Beep(1000,3000) 
                
    def quitFunction(self):
        self.close()

# QApplication은 GUI를 움직이게 해주는 클래스
# exec_()라는 메서드를 실행해서 Qt의 시그널과 슬롯이 상호작용하게끔 이벤트루프를 시작하는 클래스
# 프로그램 내에서 꼭 한 번 실행되어야 하며, 한 개의 인스턴스만 존재
app=QApplication(sys.argv)  # app 생성
win=BeepSound()             # BeepSound() 생성. QMainWindow를 띄움, 이를 Window라 함
win.show()                  # Window를 보임
app.exec_()                 # app무한루프 : 이벤트 처리
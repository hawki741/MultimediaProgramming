import cv2 as cv 
import sys
import numpy as np

#img=cv.imread('soccer.jpg')
img = np.zeros((600,800,3), np.uint8)   # 400*600 크기, 3바이트(unsignd int, 1바이트)
img[:] = (255,255,255)                  # 행열을 흰색으로 초기화

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

BrushSiz=5					            # 붓의 크기
LColor,RColor=(255,0,0),(0,0,255)		# 파란색과 빨간색

def draw(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:   
        cv.circle(img,(x,y),BrushSiz,LColor,-1)# 마우스 왼쪽 버튼 클릭하면 파란색
    elif event==cv.EVENT_RBUTTONDOWN: 
        cv.circle(img,(x,y),BrushSiz,RColor,-1)# 마우스 오른쪽 버튼 클릭하면 빨간색
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),BrushSiz,LColor,-1)# 왼쪽 버튼 클릭하고 이동하면 파란색
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img,(x,y),BrushSiz,RColor,-1)# 오른쪽 버튼 클릭하고 이동하면 빨간색

    cv.imshow('Painting',img)		# 수정된 영상을 다시 그림

cv.namedWindow('Painting')
cv.imshow('Painting',img)

cv.setMouseCallback('Painting',draw)

while(True):
    key = cv.waitKey(1)
    if key==ord('s'):       # s 키를 누르면 저장
        cv.imwrite('my_painter.png',img)
    elif key==ord('q'):
        cv.destroyAllWindows()      
        break
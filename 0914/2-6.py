import cv2 as cv
import sys

img=cv.imread('girl_laughing.jpg') 
  
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.rectangle(img,(830,30),(1000,200),(0,0,255),2)	# 직사각형 그리기
cv.putText(img,'laugh',(830,24),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)	# 글씨 쓰기

cv.line(img, (50,50), (250,150), (255,0,0), 3)

cv.rectangle(img, (50,50), (250,150), (0,255,0), 2)
cv.rectangle(img, (50,200), (250,300), (0,255,0), cv.FILLED)

cv.circle(img, (320,100), 50, (0,0,255), 4)
cv.circle(img, (320,250), 30, (0,255,255), -1)

cv.putText(img, "text1", (400,50), cv.FONT_HERSHEY_DUPLEX, 1, (128, 128, 0), 2)
cv.putText(img, "text2", (400,200), cv.FONT_HERSHEY_TRIPLEX, 2, (221, 160, 221), 4)

cv.imshow('Draw',img)

cv.waitKey()
cv.destroyAllWindows()
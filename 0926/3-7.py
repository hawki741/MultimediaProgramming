import cv2 as cv
import numpy as np

img=cv.imread('soccer.jpg')
img=cv.resize(img,dsize=(0,0),fx=0.4,fy=0.4)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.putText(gray,'soccer',(10,20),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
cv.imshow('Original',gray)

smooth=np.hstack((cv.GaussianBlur(gray,(5,5),0.0),cv.GaussianBlur(gray,(9,9),0.0),cv.GaussianBlur(gray,(15,15),0.0)))
# 두번째 인자인 필터의 크기가 클수록 블러링 효과 커짐
# 세번째 인자인 sigma는 보통 0
#cv.imshow('Smooth',smooth)

femboss=np.array([[-1.0, 0.0, 0.0],
                  [ 0.0, 0.0, 0.0],
                  [ 0.0, 0.0, 1.0]])

gray16=np.int16(gray) # gray는 1바이트(8bits) => 16bit
# int8로 음수를 표현하는 경우 -128~127까지만 표현 가능
emboss=np.uint8(np.clip(cv.filter2D(gray16,-1,femboss)+128,0,255)) # 0보다 작으면 0, 255보다 크면 255
emboss_bad=np.uint8(cv.filter2D(gray16,-1,femboss)+128) # -255(0-255) ~ 255(255-0)
emboss_worse=cv.filter2D(gray,-1,femboss)       # gray16 : -255(0-255) ~ 255(255-0)

cv.imshow('Emboss',emboss)
#cv.imshow('Emboss_bad',emboss_bad)
#cv.imshow('Emboss_worse',emboss_worse)

cv.waitKey()
cv.destroyAllWindows()
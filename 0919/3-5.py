import cv2 as cv
import numpy as np

img=cv.imread('soccer.jpg') 
img=cv.resize(img,dsize=(0,0),fx=0.25,fy=0.25)

def gamma(f,gamma=1.0):
    f1=f/255.0			# L=256이라고 가정 : 감마 연산을 위해 0 ~ 1 실수로
    return np.uint8(255*(f1**gamma)) # 감마 연산 후 다시 0 ~ 255 : 1바이트 정수로

gc=np.hstack((gamma(img,0.5),gamma(img,0.75),gamma(img,1.0),gamma(img,2.0),gamma(img,3.0)))
cv.imshow('gamma',gc)

cv.waitKey()
cv.destroyAllWindows()
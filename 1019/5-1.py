import cv2 as cv
import numpy as np

img=np.array([[0,0,0,0,0,0,0,0,0,0],	# 10 * 10 영상
              [0,0,0,0,0,0,0,0,0,0],	# 0은 배경, 1은 물체
              [0,0,0,1,0,0,0,0,0,0],
              [0,0,0,1,1,0,0,0,0,0],
              [0,0,0,1,1,1,0,0,0,0],
              [0,0,0,1,1,1,1,0,0,0],
              [0,0,0,1,1,1,1,1,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0]],dtype=np.float32)

ux=np.array([[-1,0,1]])		# x 1차 미분 필터
uy=np.array([-1,0,1]).transpose()	# y 1차 미분 필터
k=cv.getGaussianKernel(3,1)		# 가우시안 필터
g=np.outer(k,k.transpose())

dy=cv.filter2D(img,cv.CV_32F,uy)	# 영상에 x 1차 미분 컨볼루션 : dx
dx=cv.filter2D(img,cv.CV_32F,ux)	# 영상에 y 1차 미분 컨볼루션 : dy
dyy=dy*dy
dxx=dx*dx
dyx=dy*dx
gdyy=cv.filter2D(dyy,cv.CV_32F,g)  	# A 행렬의 p
gdxx=cv.filter2D(dxx,cv.CV_32F,g)   	# A 행렬의 q
gdyx=cv.filter2D(dyx,cv.CV_32F,g)   	# A 행렬의 r
C=(gdyy*gdxx-gdyx*gdyx)-0.04*(gdyy+gdxx)*(gdyy+gdxx)	# 응답함수 계산

for j in range(1,C.shape[0]-1):		# 비최대 억제
    for i in range(1,C.shape[1]-1):
        if C[j,i]>0.1 and sum(sum(C[j,i]>C[j-1:j+2,i-1:i+2]))==8:	# C[j,i] 주변의 8개 이웃에서 C[j,i]보다 작은 값을 갖는 이웃의 개수
							# 8개 즉, 모든 이웃 픽셀이 작은 값을 갖는 경우만
            img[j,i]=9			# 특징점으로 인식 : 특징점을 원본 영상에 9로 표시
                
np.set_printoptions(precision=2)
print(dy) 
print(dx) 
print(dyy) 
print(dxx) 
print(dyx) 
print(gdyy) 
print(gdxx) 
print(gdyx) 
print(C)						# 특징 가능성 맵 
print(img)					# 특징점을 9로 표시한 원본 영상 

popping=np.zeros([160,160],np.uint8)	# 화소 확인 가능하게 16배로 확대
for j in range(0,160):
    for i in range(0,160):
        popping[j,i]=np.uint8((C[j//16,i//16]+0.06)*700)  

cv.imshow('Image Display2',popping)    
cv.waitKey()
cv.destroyAllWindows()
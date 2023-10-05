import cv2 as cv

#img=cv.imread('soccer.jpg')
img=cv.imread('check.png')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray = cv.blur(gray, (3,3)) # 잡음 제거 효과

#grad_x=cv.Sobel(gray,cv.CV_32F,1,0,ksize=3)	# 소벨 연산자 적용, sobel_x
#grad_y=cv.Sobel(gray,cv.CV_32F,0,1,ksize=3) # sobel_y
grad = cv.Laplacian(gray, cv.CV_32F)

#sobel_x=cv.convertScaleAbs(grad_x)	# 절대값을 취해 양수 영상으로 변환
#sobel_y=cv.convertScaleAbs(grad_y)
lap=cv.convertScaleAbs(grad)

#edge_strength=cv.addWeighted(sobel_x,0.5,sobel_y,0.5,0)	# 에지 강도 계산
# 0.5*sobel_x + 0.5*sobel_y + 0.0

cv.imshow('Original',gray)
#cv.imshow('sobelx',sobel_x)
#cv.imshow('sobely',sobel_y)
#cv.imshow('edge strength',edge_strength)
cv.imshow('laplacian', lap)

cv.waitKey()
cv.destroyAllWindows()
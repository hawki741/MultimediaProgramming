import cv2 as cv 

img=cv.imread('apples.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

apples=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,200,param1=150,param2=80,minRadius=50,maxRadius=120)
# method : 검출방법, HOUGH_GRADIENT
# dp : 이미지해상도 : accumulator해상도, 1이면 두 해상도 같음
# dist : 검출된 원 중심 사이의 최소 거리
# param1 : canny의 높은 threshold
# param2 : 누적 threshold
# minRadius, maxRadius : 검출할 원 반지름 범위

if apples is not None :
    for i in apples[0]:
        print(i)
        cv.circle(img,(int(i[0]),int(i[1])),int(i[2]),(255,0,0),2)

cv.imshow('Apple detection',img)  

cv.waitKey()
cv.destroyAllWindows()
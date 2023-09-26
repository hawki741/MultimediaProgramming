import cv2 as cv

#gray = cv.imread('soccer.jpg', cv.IMREAD_GRAYSCALE)
#cv.imshow('original - gray', gray)

#gray_mask = cv.inRange(gray, 120,170)    # 120~170이면 white, 아니면 black
#cv.imshow('inRange', gray_mask)

img = cv.imread('soccer.jpg')
cv.imshow('original', img)

hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
red_mask = cv.inRange(hsv_img, (-10,50,50), (10,255,255)) # red의 범위
#green_mask = cv.inRange(hsv_img, (30,50,50),(70,255,255)) # green의 범위
#blue_mask = cv.inRange(hsv_img, (110,50,50),(130,255,255)) # blue의 범위

img_red = cv.bitwise_and(img, img, mask=red_mask)
# A and B : if B=0(block), 0(Black), else(B=1,white) A=0 -> 0, A=1 -> 1
# 즉, img and mask 는 mask가 black은 black으로, mask가 white는 img 값을 출력

cv.imshow('red detection', img_red)

cv.waitKey()
cv.destroyAllWindows()
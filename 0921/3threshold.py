import cv2 as cv

def onChange(value):		                                    # 트랙바 콜백 함수
    global gray, bar_name, title                        	    # 전역 변수 참조

    th = cv.getTrackbarPos(bar_name, title)
    ret, img_thresh = cv.threshold(gray, th, 255, cv.THRESH_BINARY)
    cv.imshow(title, img_thresh)

gray=cv.imread('soccer.jpg',cv.IMREAD_GRAYSCALE)

title = 'Trackbar Event'
cv.imshow(title, gray)

bar_name = "Threshold"
cv.createTrackbar(bar_name, title, gray[0][0], 255, onChange)   # 트랙바 콜백 함수 등록

cv.waitKey(0)
cv.destroyAllWindows()
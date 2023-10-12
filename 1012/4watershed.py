import cv2 as cv
import numpy as np

# Image loading
img = cv.imread("water_coins.jpg")

# image grayscale conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Threshold Processing
ret, bin_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
#cv.imshow("binarized image", bin_img)

# white(object) noise removal
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
b_opening = cv.dilate(cv.erode(bin_img,kernel,iterations=2),kernel,iterations=2)	# 열기opening
#cv.imshow("white noise removal", b_opening)

# sure background area
sure_bg = cv.dilate(b_opening,kernel,iterations=3)
cv.imshow("sure background area", sure_bg)

# sure foreground area
# distanceTransform : Binary 이미지에서  픽셀값이 0인 배경으로부터의 거리를 픽셀값이 255인 영역에 표현하는 방법
dist_transform = cv.distanceTransform(b_opening,cv.DIST_L2,5)
# 2 : 거리 공식
# 3 : 마스크 크기
dist = dist_transform * 10
dist = np.uint8(dist)
#cv.imshow("dist_transform", dist)

ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
cv.imshow("sure foreground area", sure_fg)

# unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_fg)
cv.imshow("unknown region", unknown)

# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)  # 각 connectedComponent마다 0부터 숫자 부여
markers = markers+1 # 숫자를 1부터로 변경
markers[unknown==255] = 0 # 숫자 0을 unknown을 표시하는데 사용

markers = cv.watershed(img,markers) # watershed : 물을 채워가면서 unknown을 connectedComponent 숫자 부여
img[markers == -1] = [255,0,0]  # watershed : 영역 분할이 되는 지점은 -1을 부여
cv.imshow("watershed results", img)

cv.waitKey()
cv.destroyAllWindows()
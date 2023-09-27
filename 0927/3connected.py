import cv2 as cv
import sys

gray = cv.imread('coins.png', cv.IMREAD_GRAYSCALE)

if gray is None:
    sys.exit('파일을 찾을 수 없습니다.')

median = cv.medianBlur(gray, 3)
_, gray_bin = cv.threshold(median, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

cnt, labels, stats, centroids = cv.connectedComponentsWithStats(gray_bin)
# cv.connectedComponentsWithStats의 입력영상은 배경은 black, 물체는 white인 이진 영상

dst = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)  # 색상 사각형을 그리기 위해 color로 변환

for i in range(1, cnt): # 각각의 객체 정보에 들어가기 위해 반복문. 범위를 1부터 시작한 이유는 배경을 제외
    (x, y, w, h, area) = stats[i]

    # 노이즈 제거
    if area < 20:       # 크기가 작은 연결요소는 무시, 사각형 그리지 않음
        continue

    cv.rectangle(dst, (x, y, w, h), (255, 0, 255), 2)
    #cv.rectangle(dst, (x, y), (x+w, y+h), (255, 0, 255), 2)

cv.imshow('original', gray)
cv.imshow('binarization', gray_bin)
cv.imshow('dst', dst)

cv.waitKey()
cv.destroyAllWindows()
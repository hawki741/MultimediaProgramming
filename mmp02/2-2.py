import cv2 as cv
import sys

img=cv.imread('soccer.jpg')	# 영상 읽기
print(type(img))
print(img.shape)

print(img[850][50][0], img[850][50][1], img[850][50][2])
print(img[450][500][0], img[450][500][1], img[450][500][2])
print(img[450][1000][0], img[450][1000][1], img[450][1000][2])

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('Image Display',img)	# 윈도우에 영상 표시

cv.waitKey()
cv.destroyAllWindows()
import cv2 as cv

#img=cv.imread('soccer.jpg')
gray=cv.imread('soccer.jpg', cv.IMREAD_GRAYSCALE)

#t,bin_img=cv.threshold(img[:,:,2],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
t,bin_img=cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print('오츄 알고리즘이 찾은 최적 임곗값=',t)

#cv.imshow('R channel',img[:,:,2])			# R 채널 영상
cv.imshow('Gray',gray)			# gray 영상
cv.imshow('Gray binarization',bin_img)	# R 채널 이진화 영상

cv.waitKey()
cv.destroyAllWindows()
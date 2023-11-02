import cv2 as cv

img=cv.imread('mot_color70.jpg') # 영상 읽기
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift=cv.SIFT_create() 
kp,des=sift.detectAndCompute(gray,None)
# sift.detectAndCompute(inputImg,mask=None)
# 특징점 검출과 특징 디스크립터 계산을 한 번에 수행
# 2mask : 특징점 검출에 사용할 필터

print(len(kp))
print(kp[0].pt, kp[0].size, kp[0].octave, kp[0].angle)
print(des[0])

gray=cv.drawKeypoints(gray,kp,None,flags=cv.DRAW_MATCHES_FLAGS_DEFAULT) #cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# drawKeypoints(inputImg,kp,outImg=None,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# flags : cv.DRAW_MATCHES_FLAGS_DEFAULT, cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
#   cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG, cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
cv.imshow('sift', gray)

k=cv.waitKey()
cv.destroyAllWindows()
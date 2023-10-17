import numpy as np
import cv2 as cv

img = cv.imread('shapes2.png')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny=cv.Canny(gray,100,200)
contours,hierarchy=cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

cv.drawContours(img,contours,-1,(255,0,255),2)

for i, contour in enumerate(contours):  # 모든 countours에 대해
    m=cv.moments(contour)				# 몇 가지 특징
    print(m)

    area=cv.contourArea(contour)        # Contour 면적
    cx,cy=m['m10']/m['m00'],m['m01']/m['m00']
    perimeter=cv.arcLength(contour,True)    # Contour 둘레 길이
    roundness=(4.0*np.pi*area)/(perimeter*perimeter)
    print(i,' : 면적=',area,'\n중점=(',cx,',',cy,')','\n둘레=',perimeter,'\n둥근 정도=',roundness)
    cv.putText(img, str(i), (int(cx), int(cy)), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0,255,0), 2)

cv.imshow('contours',img)

cv.waitKey()
cv.destroyAllWindows()
import cv2 as cv
import numpy as np

img = np.zeros((600,800,3), np.uint8)   # 400*600 크기 * 3바이트 * unsigned int(1바이트)
img[:] = (255,255,255)                  # 행렬을 흰색(바탕색)으로 초기화

BrushSiz = 5                            # 원의 반지름(붓의 두께로 사용할 에정)
LColor,RColor = (255,0,0),(0,0,255)		# 파란색과 빨간색

def painting(event,x,y,flags,param):
    global ix,iy

    if event==cv.EVENT_LBUTTONDOWN or event==cv.EVENT_RBUTTONDOWN:      # 마우스 버튼 다운하면
        ix, iy = x, y
    elif event==cv.EVENT_LBUTTONUP and flags==cv.EVENT_FLAG_SHIFTKEY:   # 마우스 왼쪽 버튼+Shift 업하면
        cv.line(img, (ix, iy), (x, y), (0, 255, 0), 2)
    elif event==cv.EVENT_LBUTTONUP and flags==cv.EVENT_FLAG_ALTKEY:
        cv.rectangle(img, (ix, iy), (x, y), (0, 255, 255), 2)
    elif event==cv.EVENT_LBUTTONUP and flags==cv.EVENT_FLAG_CTRLKEY:
        r = np.sqrt((x - ix) * (x - ix) + (y - iy) * (y - iy))
        cv.circle(img, (ix, iy), r.astype('i'), (255, 0, 255), 2)
    elif event==cv.EVENT_RBUTTONUP and flags==cv.EVENT_FLAG_ALTKEY:     # 마우스 오른쪽 버튼+Alt 업하면
        cv.rectangle(img, (ix, iy), (x, y), (0, 255, 255), -1)
    elif event==cv.EVENT_RBUTTONUP and flags==cv.EVENT_FLAG_CTRLKEY:
        r = np.sqrt((x - ix) * (x - ix) + (y - iy) * (y - iy))
        cv.circle(img, (ix, iy), r.astype('i'), (255, 0, 255), -1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:    # 마우스 왼쪽 버튼을 눌르면서 움직이면
        cv.circle(img,(x,y),BrushSiz,LColor,-1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:    # 마우스 오른쪽 버튼을 눌르면서 움직이면
        cv.circle(img,(x,y),BrushSiz,RColor,-1)

    cv.imshow('HW1 - Painting',img)		# 수정된 영상을 다시 그림

cv.namedWindow('HW1 - Painting')
cv.imshow('HW1 - Painting',img)

cv.setMouseCallback('HW1 - Painting',painting)

while(True):
    key = cv.waitKey(1)
    if key == ord('s'):	                # 's' 키를 누르면
        cv.imwrite('painter.png', img)  # 이미지를 저장
    if key == ord('q'):
        cv.destroyAllWindows()
        break
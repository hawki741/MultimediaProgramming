import cv2 as cv
import numpy as np

img = cv.imread('rose.png')

def rotate(event,x,y,flags,param):
    global img

    rows, cols = img.shape[:2]
    if event == cv.EVENT_LBUTTONDOWN :
        # 90 반시계 rotate
        src_points = np.float32([[0, 0], [0, rows - 1], [cols - 1, 0]])
        dst_points = np.float32([[0, cols - 1], [rows - 1, cols - 1], [0, 0]])

        affine_matrix = cv.getAffineTransform(src_points, dst_points)
        img = cv.warpAffine(img, affine_matrix, (rows, cols))  # 90 회전후 영상 크기

    elif event == cv.EVENT_RBUTTONDOWN :
        # 90 시계 rotate
        src_points = np.float32([[0, rows - 1], [cols - 1, rows - 1], [0, 0]])
        dst_points = np.float32([[0, 0], [0, cols - 1], [rows - 1, 0]])

        affine_matrix = cv.getAffineTransform(src_points, dst_points)
        img = cv.warpAffine(img, affine_matrix, (rows, cols))  # 90 회전후 영상 크기

    cv.imshow('90Rotate',img)		# 수정된 영상을 다시 그림

cv.namedWindow('90Rotate')
cv.imshow('90Rotate',img)

cv.setMouseCallback('90Rotate',rotate)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break
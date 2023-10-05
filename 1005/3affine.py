import cv2 as cv
import numpy as np

img=cv.imread('rose.png')

rows, cols = img.shape[:2] # shape : 행렬의 크기(세로,가로)

#Horizontal 좌우 대칭
#src_points = np.float32([[0,0], [cols-1,0], [0,rows-1]])
#dst_points = np.float32([[cols-1,0], [0,0], [cols-1,rows-1]])

#Vertical 상하 대칭
#src_points = np.float32([[0,0], [cols-1,0], [0,rows-1]])
#dst_points = np.float32([[0,rows-1], [cols-1,rows-1], [0,0]])

#Origin 원점 대칭
#src_points = np.float32([[0,0], [0,rows-1], [cols-1,0]])
#dst_points = np.float32([[cols-1,rows-1], [cols-1,0], [0, rows-1]])

#90 반시계방향 rotate
src_points = np.float32([[0,0], [0,rows-1], [cols-1,0]])
dst_points = np.float32([[0,cols-1], [rows-1,cols-1], [0, 0]])

affine_matrix = cv.getAffineTransform(src_points, dst_points)
#img_symmetry = cv.warpAffine(img, affine_matrix, (cols,rows)) # 세번째 인자 출력 영상의 크기(가로,세로)
img_symmetry = cv.warpAffine(img, affine_matrix, (rows,cols))

cv.imshow('Original',img)
cv.imshow('Symmetry',img_symmetry)

cv.waitKey()
cv.destroyAllWindows()
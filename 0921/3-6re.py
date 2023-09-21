import cv2 as cv
import matplotlib.pyplot as plt

#img=cv.imread('mistyroad.jpg')
#img=cv.imread('CT-brain-image.jpg')
img=cv.imread('CT-image.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)		# 명암 영상으로 변환하고 출력

fig = plt.figure(figsize=(10,10))
rows = 2
cols = 2

ax1 = fig.add_subplot(rows, cols, 1)
ax1.imshow(gray, cmap='gray')               # 1 입력 영상 출력
ax1.axis("off")

ax2 = fig.add_subplot(rows, cols, 2)
h=cv.calcHist([gray],[0],None,[256],[0,256])	# 히스토그램
ax2.plot(h,color='r',linewidth=1)               # 2 히스토그램 출력

equal=cv.equalizeHist(gray)			            # 히스토그램 평활화
ax3 = fig.add_subplot(rows, cols, 3)
ax3.imshow(equal, cmap='gray')                  # 3 히스토그램 평활화 결과 출력
ax3.axis("off")

ax4 = fig.add_subplot(rows, cols, 4)
h=cv.calcHist([equal],[0],None,[256],[0,256])	# 평활화 결과 이미지의 히스토그램
ax4.plot(h,color='r',linewidth=1)               # 4 평활화 결과 이미지의 히스토그램 출력

plt.show()

import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('soccer.jpg')     # bgr
cv.imshow('opencv', img)

img2= cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img2)                 # rgb
plt.show()

h=cv.calcHist([img],[2],None,[256],[0,256]) # 2번 채널인 R 채널에서 히스토그램 구함
plt.plot(h,color='r',linewidth=1)

hg=cv.calcHist([img],[1],None,[256],[0,256]) # 1번 채널인 G 채널에서 히스토그램 구함
plt.plot(hg,color='g',linewidth=2, linestyle="dotted")

hb=cv.calcHist([img],[0],None,[256],[0,256]) # 0번 채널인 B 채널에서 히스토그램 구함
plt.plot(hb,color='b',linewidth=3, linestyle="dashed")

plt.show()
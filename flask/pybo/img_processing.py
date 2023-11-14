import numpy as np
import cv2 as cv

def embossing(img):
    femboss = np.array([[-1.0, 0.0, 0.0],
                        [0.0, 0.0, 0.0],
                        [0.0, 0.0, 1.0]])
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray16 = np.int16(gray)  # gray는 1바이트(8bits) => 16bit
    # int8로 음수를 표현하는 경우 -128~127까지만 표현 가능
    emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))  # 0보다 작으면 0, 255보다 크면 255
    return emboss

#     def cartoonFunction(self):
#         self.cartoon=cv.stylization(self.img,sigma_s=60,sigma_r=0.45)
#         cv.imshow('Cartoon',self.cartoon)
#
#     def sketchFunction(self):
#         self.sketch_gray,self.sketch_color=cv.pencilSketch(self.img,sigma_s=60,sigma_r=0.07,shade_factor=0.02)
#         cv.imshow('Pencil sketch(gray)',self.sketch_gray)
#         cv.imshow('Pencil sketch(color)',self.sketch_color)
#
#     def oilFunction(self):
#         self.oil=cv.xphoto.oilPainting(self.img,10,1,cv.COLOR_BGR2Lab)
#         cv.imshow('Oil painting',self.oil)

def cartoon(img):
    cartoon=cv.stylization(img,sigma_s=60,sigma_r=0.45)
    return cartoon  #출력영상

def pencilGray(img):
    sketch_gray, _ = cv.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
    return sketch_gray

def pencilColor(img):
    _, sketch_color = cv.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
    return sketch_color

def oilPainting(img):
    oil = cv.xphoto.oilPainting(img, 10, 1, cv.COLOR_BGR2Lab)
    return oil

def detailEnhance(img):
    detail = cv.detailEnhance(img, sigma_s=10,sigma_r=0.15)
    # detailEnhance()는 이미지의 세부 내용을 향상 시켜주는 필터 함수
    # sigma_s : 이미지가 얼마나 부드러워지는지를 제어. 값이 클수록 더 부드러워지지만 속도도 느려집니다.
    # sigma_r : 가장자리(에지)를 얼마나 유지하려는지를 제어. 작은 값은 매우 유사한 색상만 부드럽게 하고, 많이
    #           많이 다른 색상은 그대로 둠.
    return detail
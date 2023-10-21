import cv2 as cv
import sys

#cap = cv.VideoCapture(0, cv.CAP_DSHOW)  # 동영상을 가져오는 클래스
cap = cv.VideoCapture('face2.mp4')

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

mode = 0    # 0은 hsv, 1은 ycbcr

while True:  # 무한루프로
    ret, frame = cap.read()  # 비디오를 구성하는 프레임 획득(frame)

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    if mode == 0:   # hsv
        img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        skin_mask = cv.inRange(img, (0, 70, 50), (50, 150, 255))  # hsv skin color 범위
        mode_str = "HSV"
    else : # 1: # ycbcr
        img = cv.cvtColor(frame, cv.COLOR_BGR2YCrCb)
        skin_mask = cv.inRange(img, (0, 133, 77), (255, 173, 127))  # ycbcr skin color 범위
        mode_str = "YCrCb"

    img_skin = cv.bitwise_and(frame, frame, mask=skin_mask)

    cv.putText(img_skin, mode_str, (50, 50), cv.FONT_HERSHEY_DUPLEX, 1, (0, 128, 128), 2)
    cv.imshow('skin color detection', img_skin)

    key = cv.waitKey(1)
    if key == ord('y'):
        mode = 1
    elif key == ord('h'):
        mode = 0
    elif key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

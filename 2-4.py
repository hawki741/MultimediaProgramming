import cv2 as cv
import sys

#cap=cv.VideoCapture(0,cv.CAP_DSHOW)	# 카메라와 연결 시도
cap=cv.VideoCapture('../ch10/slow_traffic_small.mp4')    # 동영상 파일

if not cap.isOpened():      # 동영상을 성공적으로 가져왔는지 확인
    sys.exit('카메라 연결 실패')
    
while True:
    ret,frame=cap.read()			# 비디오를 구성하는 프레임 획득
    # ret는 프레임을 성공적으로 가져오면 true, 그렇지 않으면(동영상 종료) false

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # BGR 컬러 영상을 명암 영상으로 변환
    gray_small = cv.resize(gray, dsize=(0, 0), fx=0.5, fy=0.5)  # 반으로 축소

    cv.imshow('Video display',gray_small)
    
    key=cv.waitKey(1)	# 1밀리초 동안 키보드 입력 기다림
    if key==ord('q'):	# 'q' 키가 들어오면 루프를 빠져나감
        break 
    
cap.release()			# 카메라와 연결을 끊음
cv.destroyAllWindows()
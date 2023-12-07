import cv2 as cv
import mediapipe as mp

# mp_holistic = human pose + face landmarks + hands
mp_holistic=mp.solutions.holistic
mp_drawing=mp.solutions.drawing_utils
mp_styles=mp.solutions.drawing_styles

holistic=mp_holistic.Holistic(static_image_mode=False,enable_segmentation=True,
                              refine_face_landmarks=True)

cap=cv.VideoCapture(0,cv.CAP_DSHOW)

while True:
    ret,frame=cap.read()
    if not ret:
      print('프레임 획득에 실패하여 루프를 나갑니다.')
      break
    
    res=holistic.process(cv.cvtColor(frame,cv.COLOR_BGR2RGB))
    
    mp_drawing.draw_landmarks(frame,res.pose_landmarks,mp_holistic.POSE_CONNECTIONS,landmark_drawing_spec=mp_styles.get_default_pose_landmarks_style())
    mp_drawing.draw_landmarks(frame,res.face_landmarks,mp_holistic.FACEMESH_TESSELATION,
                              landmark_drawing_spec=None,
                              connection_drawing_spec=mp_styles.get_default_face_mesh_tesselation_style())
    mp_drawing.draw_landmarks(frame,res.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                              landmark_drawing_spec=mp_styles.get_default_hand_landmarks_style(),
                              connection_drawing_spec=mp_styles.get_default_hand_connections_style())
    mp_drawing.draw_landmarks(frame, res.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                              landmark_drawing_spec=mp_styles.get_default_hand_landmarks_style(),
                              connection_drawing_spec=mp_styles.get_default_hand_connections_style())

    print(res.pose_landmarks)
    print('===================================')

    cv.imshow('MediaPipe pose',cv.flip(frame,1)) # 좌우반전
    if cv.waitKey(5)==ord('q'):
      #mp_drawing.plot_landmarks(res.pose_world_landmarks,mp_holistic.POSE_CONNECTIONS)
      break

cap.release()
cv.destroyAllWindows()
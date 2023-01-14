import cv2
import mediapipe as mp

# variables made for convenience
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_pose=mp.solutions.pose

cap=cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence = 0.5,min_tracking_confidence = 0.5) as pose:
    # while webcam is running
    while cap.isOpened():
        success, image = cap.read()
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        #drawing indication lines
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
        )

        #flip image horizontally for mirrored view
        cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))

        #stops running webcam until 'q' is clicked 
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()        

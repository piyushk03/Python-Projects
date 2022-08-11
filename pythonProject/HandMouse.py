import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width , screen_height = pyautogui.size()
index_y = 0
while 1:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)   #0 means flip around x axis and 1 means flip around y axis
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):   #to get index position of landmarks
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255)) #Draw a yellow cirle of radius 10 pixel with centers as x,y on the tip of index finger 
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255)) #Draw a yellow cirle of radius 10 pixel with centers as x,y on the tip of thumb
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 30:
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('Virtul Mouse',frame)
    cv2.waitKey(1)
    
import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

tipIds = [4,8,12,16,20]

def countiboi(img,hand_landMarks,hand_no=0):
    if hand_landMarks:
        landMarks = hand_landmarks[hand_no].landmark
        fingers = []
        for lm_index in tipIds:
            finger_tip_y = landMarks[lm_index].y
            finger_bottome_y = landMarks[lm_index-2].y

            if lm_index!=4:
                if finger_tip_y<finger_bottome_y:
                    fingers.append(1)
                    print (lm_index,"ffs lmao ur bad also it is opende lmao bad lmao")
                if finger_tip_y>finger_bottome_y:
                    fingers.append(0)
                    print (lm_index,"ffs lmao ur bad also it is not opende lmao bad lmao")

        total_fingers = fingers.count(1)
        text = f'Fingers: {total_fingers}'
        cv2.putText(image, text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

        
                
                

hands = mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)
def drawHandMarks(image,hand_landmarks):
    if hand_landmarks:
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(image,landmarks,mp_hands.HAND_CONNECTIONS)



while True:
    success, image = cap.read()
    image = cv2.flip(image,1)
    results = hands.process(image)

    hand_landmarks = results.multi_hand_landmarks
    drawHandMarks(image,hand_landmarks)

   

    
    cv2.imshow("Media Controller", image)
    
    
    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()


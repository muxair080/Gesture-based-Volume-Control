import cv2
import time
import mediapipe as mp 
class handDetector():
    def __init__(self, mode=False, maxHands=2, 
    detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = 2
        self.detectionCon = int(detectionCon)
        self.trackCon = int(trackCon)

        self.mpHands = mp.solutions.hands 
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
        self.detectionCon, self.trackCon)

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                for id, lm in enumerate(handlms.landmark):
                    if draw:
                        self.mpDraw.draw_landmarks(img,
                            handlms, self.mpHands.HAND_CONNECTIONS)
            
        return img 


    def findPosition(self, img, handNo=0, draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255,0,0), cv2.FILLED)
            
        return lmlist




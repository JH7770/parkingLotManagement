import cv2
import pickle
import numpy as np
from time import sleep

cap = cv2.VideoCapture('carPark.mp4')

width, height = 107, 48
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

print((posList))

while True:
    # Get image frame
    success, ori = cap.read()
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)


    img = cv2.Canny(ori, 50, 200)
    isCar = [False] * len(posList)

    for i, pos in enumerate(posList):
        x, y = pos
        x2, y2 = x + width, y+height
        img_trim = img[y:y2, x:x2]
        # cv2.imshow(str(i), img_trim)

        mean = cv2.mean(img_trim)[0]
        if mean > 25:
            isCar[i] = True
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    for i, pos in enumerate(posList):
        color = (0, 255, 0) if isCar[i] else (0, 0, 255)

        x, y = pos
        x2, y2 = x + width, y + height
        cv2.putText(ori ,str(i), (int(x+width/2), y2), cv2.FONT_HERSHEY_PLAIN, 2, color, 1, cv2.LINE_AA)
        cv2.rectangle(ori, (x, y), (x2, y2), color, thickness=3)

    cv2.imshow("ori", ori)
    cv2.imshow("img", img)

    key = cv2.waitKey(1)
    if key == ord('r'):
        break

    sleep(1)
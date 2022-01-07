from typing import List, Tuple

import cv2
import pickle
import numpy as np
from time import sleep, time

from multiprocessing import Process
from operator import itemgetter

width, height = 107, 48

__all__ = ["track_always_by_multiprocessing"]


def get_pos_list():
    ret = []
    try:
        with open('resources/CarParkPos', 'rb') as f:
            posList = pickle.load(f)
    except:
        return []

    posList = sorted(posList, key=lambda x: x[0] + x[1])
    posList = sorted(posList, key=itemgetter(0))

    column_range: list[tuple[int, int]] = [(0, 100), (100, 200), (350, 450), (450, 550), (700, 800), (850, 950)]
    for l, r in column_range:
        ret.extend(sorted([pos for pos in posList if l < pos[0] < r], key=itemgetter(1)))


    return ret

def check_car_coordinate(img, posList):
    isCar = [False] * len(posList)

    for i, pos in enumerate(posList):
        x, y = pos
        x2, y2 = x + width, y + height
        img_trim = img[y:y2, x:x2]
        # cv2.imshow(str(i), img_trim)

        mean = cv2.mean(img_trim)[0]
        if i == 13:
            print(i, mean)
        if mean > 25:
            isCar[i] = True
    return isCar




def track_always():
    cap = cv2.VideoCapture('resources/carPark.mp4')
    posList = get_pos_list()
    start = time()
    while True:
        # Get image frame
        success, ori = cap.read()

        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        end = time()
        duration = end - start
        if duration < 3:
            sleep(0.1)
            continue
        else:
            start = time()

        img = cv2.Canny(ori, 50, 200)
        # img = cv2.

        isCar = check_car_coordinate(img, posList)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        for i, pos in enumerate(posList):
            color = (0, 0, 255) if isCar[i] else (0, 255, 0)
            x, y = pos
            x2, y2 = x + width, y + height
            cv2.putText(ori, str(i), (int(x + width / 2), y2), cv2.FONT_HERSHEY_PLAIN, 2, color, 1, cv2.LINE_AA)
            cv2.rectangle(ori, (x, y), (x2, y2), color, thickness=3)
        #
        cv2.imshow("ori", ori)
        cv2.imshow("img", img)
        key = cv2.waitKey(1)
        if key == ord('r'):
            break

        # sleep(1)


def track_always_by_multiprocessing():
    p = Process(target=track_always)
    p.start()
    p.join()

from typing import List, Tuple

import cv2
import pickle
import numpy as np
from time import sleep, time
from operator import itemgetter

width, height = 107, 48


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


def draw_car_status(img, posList, isCar):
    for i, pos in enumerate(posList):
        color = (0, 0, 255) if isCar[i] else (0, 255, 0)
        x, y = pos
        x2, y2 = x + width, y + height
        cv2.putText(img, str(i), (int(x + width / 2), y2), cv2.FONT_HERSHEY_PLAIN, 2, color, 1, cv2.LINE_AA)
        cv2.rectangle(img, (x, y), (x2, y2), color, thickness=3)

    return img


def track_always_and_save_status():
    """
    자동차의 좌표 확인 후 상태 저장
    :return:
    """
    cap = cv2.VideoCapture('resources/carPark.mp4') # get video file
    posList = get_pos_list() # car position (coordinates)
    start = time()
    while True:
        # Get image frame
        success, ori = cap.read()

        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        # check car status every 3 secs
        end = time()
        if end - start < 3:
            sleep(0.1)
            continue

        start = time()

        # image preprocessing
        img = cv2.Canny(ori, 50, 200)

        #  check if there's a car in the coordinates
        isCar = check_car_coordinate(img, posList)

        # draw to image
        draw_image = draw_car_status(ori, posList, isCar)

        cv2.imshow("ori", draw_image)
        cv2.imshow("img", img)
        key = cv2.waitKey(1)
        if key == ord('r'):
            break

        # sleep(1)

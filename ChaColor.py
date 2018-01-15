import numpy as np
import cv2

def hsv():#Hue(색상), Saturation(채도), Value(진하기)
    blue = np.uint8([[[255, 0, 0]]])
    green = np.uint8([[[0, 255, 0]]])
    red = np.uint8([[[0, 0, 255]]])
    #각 색 픽셀 1개에 해당하는 numpy array를 생성합니다.

    hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
    #BGR 색공간으로 생성한 색들을 HSV 값으로 전환한 것을 hsv_색에 담는다.

    print('HSV for BLUE', hsv_blue)
    print('HSV for green', hsv_green)
    print('HSV for red', hsv_red)

hsv()

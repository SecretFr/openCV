import numpy as np
import cv2

def onChange(x):#트랙바 이벤트를 처리할 콜백함수, 트랙바 이벤트가 발생할 때 처리할 일이 아무것도 없으므로 그냥 pass
    pass

def trackbar():
    img = np.zeros((200, 512, 3), np.uint8)
    cv2.namedWindow('color_palette')

    cv2.createTrackbar('B', 'color_palette', 0, 255, onChange)
    cv2.createTrackbar('G', 'color_palette', 0, 255, onChange)
    cv2.createTrackbar('R', 'color_palette', 0, 255, onChange)

    switch = '0: OFF\n1: ON'
    cv2.createTrackbar(switch, 'color_palette', 0, 1, onChange)
    #트랙바를 지정된 윈도에 생성하는 함수, 트랙바 생성
    while True:
        cv2.imshow('color_palette', img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27
            break

        b = cv2.getTrackbarPos('B', 'color_palette')
        g = cv2.getTrackbarPos('G', 'color_palette')
        r = cv2.getTrackbarPos('R', 'color_palette')
        s = cv2.getTrackbarPos(switch, 'color_palette')
        #트랙바의 현재 위치를 리턴하는 함수
        if s == 0:
            img[:] = 0
            #스위치가 off이면 그림판 색상을 검정색으로 만듬
        else:
            img[:] = [b, g, r]
            #스위치가 on이면 그림판 색상을 채움
    cv2.destroyAllWindows()

trackbar()

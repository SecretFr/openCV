import numpy as np
import cv2

#이미지 비트 연산은 이미지에서 특정 영역을 추출하거나 직사각형 모양이 아닌 ROI를 정의하거나 할 때 매우 유용하다
def bitOperation(hpos, vpos):#인자로 로고가 있을 좌표를 받는다.
    img1 = cv2.imread('images/sana.jpg')
    img2 = cv2.imread('images/logo.jpg')

    #로고를 사나 사진 왼쪽 윗부분에 두기 위해 해당 영역 지정
    rows, cols, channels = img2.shape#로고 이미지의 크기를 구한다.
    print(rows)
    print(cols)
    print(channels)
    roi = img1[vpos:rows+vpos, hpos:cols+hpos]#img1에서 로고를 위한 영역 roi를 잡는다.

    #로고를 위한 마스크와 역마스트 생성하기
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    #이미지를 먼저 흑백으로 변환, 마스크를 만든다, 흑과 백으로 완전히 구분
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    #마스크를 씌운 후 연산을 하게 되면 특정한 효과를 낼 수가 있게 된다.
    mask_inv = cv2.bitwise_not(mask)#배경이 백, 나머지 흑

    #roi에서 로고에 해당하는 부분만 검정색으로 만들기
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    #mask 값이 0이 아닌 부분(흰색=1)만 AND 연산, 따라서 검정색(0) 그대로 이미지에 놓여짐

    #로고 이미지에서 로고 부분만 추출하기
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    #로고 이미지 배경을 cv2.add로 투명으로 만들고 roi에 로고이미지 넣기
    dst = cv2.add(img1_bg, img2_fg)
    #검정 픽셀값이 0이므로 두 이미지를 더하게 되면 검정색은 없어지고 검정색 아닌 색이 표출
    img1[vpos:rows+vpos, hpos:cols+hpos] = dst

    cv2.imshow('result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bitOperation(10, 10)

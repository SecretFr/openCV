import numpy as np
import cv2

#이미지 Contour : 같은 값을 가진 곳을 연결한 선
#이미지에서 Contour를 찾기 전에 threshold나 Canny edge detection을 적용하는 것이 좋다.
#Contour를 찾고자 하는 대상은 흰색으로, 배경은 검정색으로 변경해야함

def contour():
    img = cv2.imread('images/globe.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    #imgray를 thresholding하여 그 값을 thresh로 한다.
    #이를 cv2.findContours()함수에 넘겨 contour를 찾는다.
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #thr, 이미지에서 찾은 contour, contour들 간의 계층 구조를 리턴
    #contour만 관심이 있으므로, 리턴값 3개 중 필요없는 인자는 '_'로 리턴
    #thresh: contour 찾기를 할 소스 이미지, thresholding을 통해 변환된 바이너리 이미지
    #cv2.RETR_TREE: 두 번째 인자는 contour 추출 모드이며, 2번째 리턴값이 hierarchy의 값에 영향을 준다.
    #_EXTERNAL : 이미지의 가장 바깥쪽의 contour만 추출
    #_LIST : contour 간 계층구조 상관관계를 고려하지 않고 contour를 추출
    #_CCOMP : 모든 contour를 추출한 후, 2단계 contour 계층 구조로 구성.
    #1단계 계층에서는 외곽 경계 부분을, 2단계 계층에서는 구멍의 경계부분을 나타내는 contour로 구성됨
    #_TREE : 이미지에서 모든 contour를 추출하고 contour들간의 상관관계를 추출함
    #CHAIN_APPROX_SIMPLE: contour 근사 방법
    #_APPROX_NONE : contour를 구성하는 모든 점을 저장함.
    #_APPROX_SIMPLE : contour의 수평, 수직, 대각선 방향의 점은 모두 버리고 끝 점만 남겨둠
    #예로 직사각형에서 4개의 모서리점만 남기고 다 버림
    #_APPROX_TC89_1 : Teh-Chin 연결 근사 알고리즘을 적용

    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
    #찾은 contour를 실제로 그리는 함수
    #-1 : img에 실제로 그릴 contour 인덱스 파라미터, 이 값이 음수이면 모든 contour를 그림
    #(0, 255, 0) : contour 선의 bgr 색상값, 여기서는 green
    #1: 선의 두께
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()

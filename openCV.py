import numpy as np
import cv2
import matplotlib

def showImage():
    imgfile = 'images/model.png'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    #이미지가 저장된 변수값을 인자로 전달 후 리턴하는 함수 imread
    #IMREAD_COLOR: 컬러 이미지로 로드, 이미지의 투명한 부분은 모두 무시됨. 디폴트 플래그, 정수값은 1
    #IMREAD_GRAYSCALE: 흑백 이미지로 로드함. 정수값은 0
    #IMREAD_UNCHANGED: 알파채널을 포함하여 이미지 그대로 로드함. 정수값은 -1

    cv2.namedWindow('model', cv2.WINDOW_NORMAL)
    #WINDOW_NORMAL: 원본 이미지 크기로 윈도우를 생성하여 이미지를 나타내지만 사용자가 크기를 조절할 수 있는 윈도우를 생성
    #WINDOW_AUTOSIZE: 원본 이미지 크기로 고정하여 윈도우를 생성함

    cv2.imshow('model', img)
    #cv2.imread에 의해 반환된 이미지 객체 img를 화면에 나타내기 위한 함수, 첫번째 인자는 윈도우 타이틀, 투번째 인자는 화면에 표시할 이미지 객체
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    k = cv2.waitKey(0) & 0xFF # 사용자가 임의의 key값을 입력했을 때 그 key값을 반환해서 k변수에 저장

    if k == 27:#esc를 누르면 창을 종료
        cv2.destroyAllWindows()
    elif k == ord('c'): #ord함수는 문자를 아스키 값으로 반환하는 함수이다. / c를 누르면 복사본 저장
        cv2.imwrite('images/model_copy.jpg', img)#이미지 복사본을 저장하는 함수
        cv2.destroyAllWindows()


showImage()

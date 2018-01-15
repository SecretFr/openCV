import numpy as np
import cv2

def onMouse(x):
    pass

def bluring():
    img = cv2.imread('openCV/images/model_copy.jpg')

    cv2.namedWindow('BlurPane')
    cv2.createTrackbar('BLUR_MODE', 'BlurPane', 0, 2, onMouse)
    cv2.createTrackbar('BLUR', 'BlurPane', 0, 5, onMouse)

    mode = cv2.getTrackbarPos('BLUR_MODE', 'BlurPane')
    val = cv2.getTrackbarPos('BLUR', 'BlurPane')

    while True:
        val = val*2+1

        try:
            if mode == 0:
                blur = cv2.blur(img,(val,val))#averaging blur
                #(val,val) : 필터 커널 사이즈, 두 값이 달라도 무방
            elif mode == 1:
                blur = cv2.GaussianBlur(img,(val, val), 0)
                #(val, val) : Gaussian 블러 필터, 두개의 값이 달라도 되지만, !(모두 양의 홀수)중요! 이어야 한다.
                #0: sigmaX 값 = 0, sigamY 값은 자동적으로 0으로 설정되고 GaussianBlur 필터만을 적용
                #이미지의 가우스 노이즈를 제거하는데 가장 효과적
                #필터링을 위해 공간적으로 이웃한 픽셀들만 확인하고 처리하기 떄문에 edge가 보존되지 않고 뭉개져 버린다.
                #bilateral필터는 Gaussian필터를 이용하지만 픽셀의 intensity 차이를 고려하기 때문에 edge가 보존된다.
            elif mode == 2:
                blur = cv2.medianBlur(img, val)
                #val : 커널 사이즈, val x val 크기의 박스내에 있는 모든 픽셀들의 median 값을 취해서
                #중앙에 있는 픽셀에 적용함.
                #화면에 소금-후추를 뿌린듯한 노이즈를 제거하는데 매우 효과적
            else:
                break

            cv2.imshow('BlurPane', blur)
        except:
            break

        k = cv2.waitKey(1) & 0xFF
        if k== 27:
            break

        mode = cv2.getTrackbarPos('BLUR_MODE','BlurPane')
        val = cv2.getTrackbarPos('BLUR', 'BlurPane')

    cv2.destroyAllWindows()

bluring()

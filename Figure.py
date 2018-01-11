import numpy as np
import cv2

#cv2.line(), 직선
#cv2.circle(), 원
#cv2.rectangle(), 직사각형
#cv2.ellipse(), 타원
#cv2.putText(), 텍스트 입력

def drawing():
    img = np.zeros((512, 512, 3), np.uint8)
    #도형을 그리기 위한 공간 생성 512x512 배열 , 데이터 타입 uint8
    #np.zeros : 배열을 만들고 모든값을 0으로 채우는 함수
    cv2.line(img, (0,0), (511,511), (255,0,0), 5)
    #좌표 0,0에서 511,511 까지 청색이고 두꼐5인 직선
    cv2.rectangle(img, (384, 0), (510,128), (0,255,0),3)
    #좌측상단, 우측상단, 녹색이면서 두꼐5인 직사각형
    cv2.circle(img, (447, 63), 63, (0,0,255), -1)
    #원의 중심좌표, 원의 반지름, 빨간색, 주어진색상으로 도형 채움
    cv2.ellipse(img, (256, 256), (100, 50), 30, 30, 180, (255, 0, 0), -1)
    #타원중심, 각각 장축과 단축의 1/2길이, 타원 기울기 각도, 타원 호를 그리는 시작 각도, 타원 호를 그리는 끝 각도
    #청색, 타원을 채움
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)
    #OpenCV 글자, 위치, 폰트, 폰트크기, 흰색, 굵기2
    cv2.imshow('drawing', img)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
    elif k==ord('c'):
        cv2.imwrite('images/draw.jpg', img)
        cv2.destroyAllWindows()


drawing()

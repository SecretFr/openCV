import numpy as np
import cv2

def showVideo():
    try:
        print('lunch Camera')
        cap = cv2.VideoCapture(1)
        #비디오 캡쳐를 위한 객체생성 / 인자: 장치 인덱스 또는 비디오파일 이름
    except:
        print('lunching Camera Failed!')
        return

    cap.set(3, 480)
    cap.set(4, 320)
    #3,4는 프레임의 폭과 높이 / 480x320 의 프레임 크기
    #비디오 프레임의 폭과 높이를 알고싶다면 cap.get(3), cap.get(4)의 값을 확인
    while (cap.isOpened()):#라이브로 들어오는 비디오를 프레임별로 캡쳐 및 이를 화면에 디스플레이
        ret, frame = cap.read()
        #재생되는 비디오의 한 프레임씩 읽어드린다.
        #비디오 프레임을 제대로 읽었다면 ret값이 True, 실패 False
        if ret:
            print("Read Video Success")
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            cv2.imshow('video', gray)
        if not ret:
            print("Read Video Error")

        #frame을 흑백으로 변환한다.

        #하나의 프레임은 하나의 이미지.
        k = cv2.waitKey(1) & 0xFF
        if k == 27:#esc키를 누르면 프로그램 종료
            break
    cap.release()#오픈한 cap 객체를 반드시 해제
    cv2.destroyAllWindows()

showVideo()

import numpy as np
import cv2
import matplotlib.pyplot as plt #python을 위한 플로팅 라이브러리 / 이미지 줌, 저장하기 등과 같은 다양한 기능들을 활용
#matplotlib는 RGB 모드로 컬러 이미지를 다룬다.
#따라서 OpenCV로 읽어들인 컬러 이미지 객체를 matplotlib에 그대로 사용하게 될 때 제대로 된 컬러 색상이 나오지 않는다
#matplotlib 매뉴얼 참고

def showImage():
    imgfile = 'images/model.png'
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    plt.imshow(img, cmap='gray', interpolation='bicubic')
    #화면에 이미지를 디스플레이하는 방법을 정의
    plt.xticks([])
    plt.yticks([])
    #x축, y축으로 눈금표시를 한다. 위 코드는 눈금 표시 없이 이미지를 표시하라는 코드
    plt.title('model')
    plt.show()

showImage()

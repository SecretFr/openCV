import numpy as np
import cv2
import matplotlib.pyplot as plt

#Attention!!!
#Sobel 알고리즘은 이미지가 검정색에서 흰색으로 변화될 때 양수 값을 취하고,
#흰색에서 검정색으로 변화될 때 음수 값을 취한다.
#만약 데이터 타입을 양수만 취급하는 np.uint8 또는 cv2.CV_8U로 지정하면 흰색에서 검정색으로 변화할 때
#취한 음수값을 모두 0으로 만들어 버리게 된다. 따라서 흰색에서 검정색으로의 경계를 찾지 못하게 되는 결과를 가져온다.

def grad():
    img = cv2.imread('images/box.jpg', cv2.IMREAD_GRAYSCALE)

    sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)

    tmp = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobel64f = np.absolute(tmp)
    sobelx8u2 = np.uint8(sobel64f)
    #tmp의 음수 부분을 모두 양수로 변환한 다음 uint8 형식으로 전환한다.

    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
    plt.title('original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
    plt.title('Sobel 8U'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 3), plt.imshow(sobelx8u2, cmap='gray')
    plt.title('Sobel 64F'), plt.xticks([]), plt.yticks([])

    plt.show()

grad()

import numpy as np
import cv2

img = cv2.imread('images/model.png')

b, g, r = cv2.split(img)
#원본 img를 BGR 채널별로 분리한 후 b, g, r에 저장한다.
#split함수는 성능면에서 효율적인 함수는 아니다.
#b = img[:,:,0]
#g = img[:,:,1]
#r = img[:,:,2] // split보다 Numpy 인덱싱을 활용하는 것이 더 좋다.
#img[:,:,2] = 0 어떠한 이미지의 모든 픽셀의 RED 값을 0으로 만들고자 할때 사용
print(img[100, 100])
#원본 이미지의 [100, 100]위치의 픽셀값은 [243, 246, 244]
print(b[100, 100], g[100, 100], r[100, 100])
#분리한 b, g, r의 [100, 100]위치의 값은 각각 243, 246, 244

cv2.imshow('blue channel', b)
cv2.imshow('green channel', g)
cv2.imshow('red channel', r)
#b, g, r의 값은 1채널 값으로 되어 있어서 모두 흑백 이미지로 디스플레이 된다.

merged_img = cv2.merge((b,g,r))
cv2.imshow('merged', merged_img)
#분리된 1채널들의 b,g,r을 merge함수를 이용해서 합친 후 출력
cv2.waitKey(0)
cv2.destroyAllWindows()

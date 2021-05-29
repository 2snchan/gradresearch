# video handler - dectecting edge

import cv2

src = cv2.imread("src/img.png", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

ret_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 5)
s, ret_normal = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
ret_adaptive = cv2.resize(ret_adaptive, dsize=(640,480), interpolation=cv2.INTER_AREA)
ret_normal = cv2.resize(ret_normal, dsize=(640,480), interpolation=cv2.INTER_AREA)

cv2.imshow("Normal", ret_normal)
cv2.imshow("Adaptive", ret_adaptive)
cv2.waitKey()
cv2.destroyAllWindows()
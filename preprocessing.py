# video handler - dectecting edge

import cv2

src = cv2.imread("src/img.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

gray = cv2.resize(gray, dsize=(640,480), interpolation=cv2.INTER_AREA)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)

print(type(sobel))

cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)


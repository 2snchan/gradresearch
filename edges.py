import cv2

image = cv2.imread("src/edge.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

img_canny = cv2.Canny(gray, 50, 150)
img_sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
img_lapla = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)

# img_canny = cv2.resize(img_canny, dsize=(640,480), interpolation=cv2.INTER_AREA)
# img_sobel = cv2.resize(img_sobel, dsize=(640,480), interpolation=cv2.INTER_AREA)
# img_lapla = cv2.resize(img_lapla, dsize=(640,480), interpolation=cv2.INTER_AREA)

cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge", img_canny)
cv2.imshow("Sobel Edge", img_sobel)
cv2.imshow("Laplacian Edge", img_lapla)

cv2.waitKey(0)
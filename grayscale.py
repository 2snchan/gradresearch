import cv2

image = cv2.imread("src/img.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(type(image))
print(type(gray))

image = cv2.resize(image, dsize=(640,480), interpolation=cv2.INTER_AREA)
gray = cv2.resize(gray, dsize=(640,480), interpolation=cv2.INTER_AREA)

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale", gray)

cv2.waitKey(0)
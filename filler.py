import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage.feature import canny
from skimage import morphology
from skimage.filters import sobel as skimage_sobel
src = cv2.imread("src/img.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
hist = np.histogram(gray, bins=np.arange(0,256))
markers = np.zeros_like(gray)

edges = canny(gray/255.)
filler = ndimage.binary_fill_holes(edges)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)

markers[gray < 30] = 1
markers[gray > 150] = 2

elevation_map = skimage_sobel(gray)
segmentation = morphology.watershed(elevation_map, markers)

fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(segmentation, cmap=plt.cm.gray, interpolation='nearest')
ax.axis('off')
ax.set_title('segmentation')

print(type(edges))
print(type(markers))
print(type(laplacian))

cv2.imshow("Scikit Image Sobel", elevation_map)
plt.show()

import cv2

# Görüntüyü yükleme
image = cv2.imread("C:\\Users\\Umit\Desktop\\yuz.png")
cv2.imshow("palm", image)
cv2.waitKey(0)

# Görüntüyü gri tonlamaya çevirme
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kenar algılama
edges = cv2.Canny(gray, 40, 55, apertureSize=3)
cv2.imshow("edges in palm", edges)
cv2.waitKey(0)

# Kenarları ters çevirme
edges = cv2.bitwise_not(edges)

# Sonucu kaydetme
cv2.imwrite("palmlines.jpg", edges)

# Yeni görüntüyü yükleme
palmlines = cv2.imread("palmlines.jpg")

# Orijinal görüntüyle birleştirme
img = cv2.addWeighted(palmlines, 0.3, image, 0.7, 0)

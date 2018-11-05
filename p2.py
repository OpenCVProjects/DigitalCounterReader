import numpy as np
import cv2

captura_color = cv2.imread('./capturas/capturas_0.jpg')
resized_captura_color = cv2.resize(captura_color, (captura_color.shape[1]/2, captura_color.shape[0]/2))

captura = cv2.cvtColor(resized_captura_color, cv2.COLOR_BGR2GRAY)

# resized_captura = cv2.resize(captura, (captura.shape[1]/2, captura.shape[0]/2))

blur = cv2.GaussianBlur(captura, (3, 3), 1)
t, dst = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

(_,contours,_) = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# for c in contours:
#     area = cv2.contourArea(c)
#     if area < 10000:
print (contours[0])
# cv2.drawContours(resized_captura_color, contours[2], 0, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("Captura", resized_captura_color)

# template = cv2.imread('./templates/0.png', 0)
# gauss_template = cv2.GaussianBlur(template, (3,3), 0)

cv2.waitKey()

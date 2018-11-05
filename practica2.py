import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

img_rgb = cv2.imread('./capturas/capturas_0.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('./templates/1.png', 0)
templates = glob.glob("./templates/*.png")

for templateImage in templates:
    template = cv2.imread(templateImage, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('res.png',img_rgb)

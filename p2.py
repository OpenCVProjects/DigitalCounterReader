import numpy as np
import cv2

captura = cv2.imread('./capturas/capturas_1.jpg')

# roi = captura[556:710, 1025:1440]
# roi = captura[837:1003, 1025:1440]
lecturas = [c1[556:710, 1025:144], c2[837:1003, 1025:1440], c3[1130:1300, 1025:1440]]
# roi = captura[1130:1300, 1025:1440]
for roi in lecturas:
    n1 = roi[19:140, 16:92]
    n2 = roi[19:140, 116:192]
    n3 = roi[19:140, 216:292]
    n4 = roi[19:140, 316:392]
    cv2.imshow("RR", roi)
    cv2.imshow("n1", n1)
    cv2.imshow("n2", n2)
    cv2.imshow("n3", n3)
    cv2.imshow("n4", n4)

cv2.waitKey(0)

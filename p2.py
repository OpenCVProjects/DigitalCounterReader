import numpy as np
import cv2

def nothing(x):
    pass

captura_color = cv2.imread('./capturas/capturas_1.jpg')
resized_captura_color = cv2.resize(captura_color, (captura_color.shape[1]/2, captura_color.shape[0]/2))

cv2.namedWindow("normal")
cv2.createTrackbar("Threshold value", "normal", 46, 255, nothing)
cv2.createTrackbar("Max", "normal", 110, 225, nothing)

captura_gray = cv2.cvtColor(resized_captura_color, cv2.COLOR_BGR2GRAY)

# imagen, contornos, jerarquia = cv2.findContours(dst.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# i=0
while True:

    value_threshold = cv2.getTrackbarPos("Threshold value", "normal")
    max = cv2.getTrackbarPos("Max", "normal")

    t, dst = cv2.threshold(captura_gray, value_threshold, 255, cv2.THRESH_BINARY_INV)
    canny = cv2.Canny(captura_gray, value_threshold, max)

    # imagen, contornos, jerarquia = cv2.findContours(canny.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    (_, contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # Mostramos el numero de monedas por consola
    print("He encontrado {} objetos".format(len(contornos)))

    # cv2.drawContours(resized_captura_color,contornos,-1,(0,0,255), 2)
    # cv2.imshow("contornos", original)

    i = 0
    for contorno in contornos:
        # if cv2.contourArea(contorno) > 10 and cv2.contourArea(contorno) < 100000:
            # approx = cv2.approxPolyDP(contorno,0.03*cv2.arcLength(contorno,True),True)
            # if len(approx)==4:
                # print(2)
        (x,y,w,h) = cv2.boundingRect(contorno)
        cv2.rectangle(resized_captura_color, (x,y), (x+w, y+h), (0, 255, 0), 3 )
        # (x, y, w, h) = cv2.boundingRect(contorno)
        #     cv2.rectangle(resized_captura_color, (x, y), (x+w, y+h), (0,255,0), 3)
        # cv2.putText(resized_captura_color, str(i), (x - 10, y - 10),
        #     cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)
        # i = i + 1;

    cv2.imshow("threshold", dst)
    cv2.imshow("normal", resized_captura_color)
    cv2.imshow("Canny", canny)
# cv2.imshow("contornos", imagen)
# cv2.imshow("contornos", imagen)

    key = cv2.waitKey(100)
    if key == 27:
        break

cv2.destroyAllWindows()

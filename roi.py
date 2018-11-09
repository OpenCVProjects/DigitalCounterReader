import numpy as np
import cv2
import glob

#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            #'cv2.TM_CCORR_NORMED'] , 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF_NORMED']

# captura = cv2.imread('./capturas/capturas_1.jpg')
#
# # template = cv2.imread('./templates/2.png', 0)
#
# roi = captura[556:710, 1025:1440]
#
# n1 = roi[19:135, 16:92]
# n2 = roi[19:135, 116:192]
# n3 = roi[19:135, 216:292]
# n4 = roi[19:135, 316:392]
#
# numeros = ['n1', 'n2', 'n3', 'n4']

# n1_gray = cv2.cvtColor(n2, cv2.COLOR_BGR2GRAY)
# cv2.imshow("n1", n1_gray)

templates = glob.glob("./templates/*.png")
capturas = glob.glob("./capturas/*.jpg")

for captura in capturas:
    # capt = eval(captura)

    capturada = cv2.imread(captura)
    print(captura)

    # template = cv2.imread('./templates/2.png', 0)

    roi = capturada[556:710, 1025:1440]

    n1 = roi[19:135, 16:92]
    n2 = roi[19:135, 116:192]
    n3 = roi[19:135, 216:292]
    n4 = roi[19:135, 316:392]

    numeros = ['n1', 'n2', 'n3', 'n4']

    for numero in numeros:
        num = eval(numero)
        num_gray = cv2.cvtColor(num, cv2.COLOR_BGR2GRAY)
        # cv2.imshow(capt, n1_gray)

        im = 0
        valor = 0
        mas_mejor = 0
        indice_final = 0
        indice = 0
        for templateImage in templates:
            template = cv2.imread(templateImage, 0)
            # cv2.imshow("Template_" + str(im), template)
            mejor = 0
            # print("Template Numero: ", im)
            im = im + 1
            for meth in methods:
                method = eval(meth)

                # Apply template Matching
                res = cv2.matchTemplate(num_gray,template,method)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

                # print("Metodo: ", meth)
                # print("Min Val:", min_val)
                # print("Max Val:", max_val)

                if max_val > mejor:
                    mejor = max_val
                    valor = indice
                    # print("nuevo mejor ", mejor,  meth)

            if mejor > mas_mejor:
                mas_mejor = mejor
                indice_final = valor

            indice = indice + 1

        print ("El numero es", indice_final)

cv2.waitKey(0)

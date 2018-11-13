import numpy as np
import cv2
import glob

#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            #'cv2.TM_CCORR_NORMED'] , 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF_NORMED']

templates = glob.glob("./templates/*.png")
capturas = glob.glob("./capturas/*.jpg")

f = open ('resultados.txt','w')
d = open('metodos.txt', 'w')

for captura in capturas:
    f.write('Resultados de la lectura:')
    f.write(captura)
    f.write('\n')
    capturada = cv2.imread(captura)

    s1 = capturada[556:710, 1025:1440]
    s2 = capturada[837:1003, 1025:1440]
    s3 = capturada[1130:1300, 1025:1440]

    secciones =  ['s1' , 's2', 's3']

    for seccion in secciones:
        resultado = 0

        roi = eval(seccion)

        n1 = roi[19:140, 16:92]
        n2 = roi[19:140, 116:192]
        n3 = roi[19:140, 216:292]
        n4 = roi[19:140, 316:392]

        numeros = ['n1', 'n2', 'n3', 'n4']

        for numero in numeros:
            num = eval(numero)
            num_gray = cv2.cvtColor(num, cv2.COLOR_BGR2GRAY)

            im = 0
            valor = 0
            mas_mejor = 0
            indice_final = 0
            indice = 0
            for templateImage in templates:
                template = cv2.imread(templateImage, 0)
                mejor = 0
                im = im + 1
                d.write("numero")
                d.write('\t')
                d.write(templateImage)
                d.write('\n')
                for meth in methods:
                    method = eval(meth)

                    # Apply template Matching
                    res = cv2.matchTemplate(num_gray,template,method)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

                    print(meth, min_val, max_val)

                    d.write(meth)
                    d.write('\t')
                    d.write(str(min_val))
                    d.write('\t')
                    d.write(str(max_val))
                    d.write('\n')

                    if max_val > mejor:
                        mejor = max_val
                        valor = indice

                if mejor > mas_mejor:
                    mas_mejor = mejor
                    indice_final = valor

                indice = indice + 1

            if numero == 'n1':
                resultado = resultado + indice_final * 100

            if numero == 'n2':
                resultado = resultado + indice_final * 10

            if numero == 'n3':
                resultado = resultado + indice_final

            if numero == 'n4':
                resultado = resultado + (indice_final * 0.1)

        f.write(str(resultado))
        f.write('\n')

f.close()
d.close()

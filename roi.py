import numpy as np
import cv2
import glob

#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            #'cv2.TM_CCORR_NORMED'] , 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF_NORMED']

# Obtenemos todas las imagenes de ambas ubicaciones
templates = glob.glob("./templates/*.png")
capturas = glob.glob("./capturas/*.jpg")

# Abrimos el fichero donde escribir los resultados
f = open ('resultados.txt','w')

# Recorremos cada imagen
for captura in capturas:
    f.write('Resultados de la lectura:')
    f.write(captura)
    f.write('\n')
    capturada = cv2.imread(captura, 0)

    # Definimos las regiones de la imagen que contienen la informacion
    s1 = capturada[556:710, 1025:1440]
    s2 = capturada[837:1003, 1025:1440]
    s3 = capturada[1130:1300, 1025:1440]
    secciones =  ['s1' , 's2', 's3']

    # Recorremos cada seccion para obtener los diferentes numeros
    for seccion in secciones:
        resultado = 0
        resultado2 = 0

        f.write("Seccion: ")
        f.write(seccion)
        f.write('\n')

        roi = eval(seccion)

        # Definimos la region de cada uno de los numeros
        n1 = roi[19:140, 16:92]
        n2 = roi[19:140, 116:192]
        n3 = roi[19:140, 216:292]
        n4 = roi[19:140, 316:392]
        numeros = ['n1', 'n2', 'n3', 'n4']

        # Recorremos cada uno de los numeros definidos
        for numero in numeros:
            num = eval(numero)

            f.write("Numero: ")
            f.write(numero)
            f.write('\n')

            im = 0
            valor = 0
            valor_dif = 0
            mas_mejor = 0
            mas_mejor_dif = 1
            indice_final = 0
            indice_final_dif = 0
            indice = 0

            # Compara un numero con cada una de las plantillas
            for templateImage in templates:
                template = cv2.imread(templateImage, 0)
                mejor = 0
                im = im + 1

                mejor_dif = 1

                f.write("Probabilidad de que sea la plantilla: ")
                f.write('\t')
                f.write(templateImage)
                f.write('\n')
                f.write("Metodo")
                f.write('\t\t\t\t')
                f.write('Min_Val')
                f.write('\t\t\t\t')
                f.write('Max_Val')
                f.write('\n')

                # Probamos cada metodo
                for meth in methods:
                    method = eval(meth)

                    res = cv2.matchTemplate(num, template,method)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

                    f.write(meth)
                    f.write('\t')
                    f.write(str(min_val))
                    f.write('\t')
                    f.write(str(max_val))
                    f.write('\n')

                    # Vemos el metodo de mayor probabilidad
                    if meth == 'cv2.TM_SQDIFF_NORMED':
                        if min_val < mejor_dif:
                            mejor_dif = min_val
                            valor_dif = indice
                    else:
                        if max_val > mejor:
                            mejor = max_val
                            valor = indice

                # Vemos el template de mayor probabilidad
                if mejor_dif < mas_mejor_dif:
                    mas_mejor_dif = mejor_dif
                    indice_final_dif = valor_dif

                if mejor > mas_mejor:
                    mas_mejor = mejor
                    indice_final = valor

                indice = indice + 1

            # Formamos el resultado
            if numero == 'n1':
                resultado = resultado + indice_final * 100
                resultado2 = resultado2 + indice_final_dif * 100

            if numero == 'n2':
                resultado = resultado + indice_final * 10
                resultado2 = resultado2 + indice_final_dif * 10

            if numero == 'n3':
                resultado = resultado + indice_final
                resultado2 = resultado2 + indice_final_dif

            if numero == 'n4':
                resultado = resultado + (indice_final * 0.1)
                resultado2 = resultado2 + (indice_final_dif * 0.1)

            f.write('****************************************************************')
            f.write('\n')
            f.write("El numero con mas probabilidad por cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED: ")
            f.write(str(indice_final))
            f.write('\n')
            f.write("El numero con mas probabilidad por cv2.TM_SQDIFF_NORMED: ")
            f.write(str(indice_final_dif))
            f.write('\n')
            f.write('****************************************************************')
            f.write('\n')

        f.write('************************************************************************************************')
        f.write('\n')
        f.write("El numero formado por cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED: ")
        f.write(str(resultado))
        f.write('\n')
        f.write("El numero formado por cv2.TM_SQDIFF_NORMED: ")
        f.write(str(resultado2))
        f.write('\n')
        f.write('************************************************************************************************')
        f.write('\n')

f.close()

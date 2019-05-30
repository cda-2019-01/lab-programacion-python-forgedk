##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##

import re
ListaDeArchivos = []
Archivo = open('data.csv', 'r')
PatronDeRemplazoValoresConComa = re.compile(r'(\d),')
ArchivoEnMemoria = (Archivo.readlines())
Archivo.close()
ArchivoEnMemoria = [linea.replace("\t", " ") for linea in ArchivoEnMemoria]
ArchivoEnMemoria = [linea.replace(":", " ") for linea in ArchivoEnMemoria]
ArchivoEnMemoria = [linea[:-1] for linea in ArchivoEnMemoria]
ArchivoEnMemoria = [PatronDeRemplazoValoresConComa.sub(r"\1 ", linea) for linea in ArchivoEnMemoria]
ArchivoEnMemoria = [linea.split(' ') for linea  in ArchivoEnMemoria]
CadenasTresLetras = [ (Registro[4]) for Registro in ArchivoEnMemoria]
LetrasUnicas = set(Registro for Registro in CadenasTresLetras) 
LetrasUnicas = sorted(LetrasUnicas)
ListaDeValoresPorLetra = {Letra:[] for Letra in LetrasUnicas}
for Fila in ArchivoEnMemoria:
    for ElmentoDeFila in Fila:
        if  ElmentoDeFila.isdigit():
            ListaDeValoresPorLetra.get(Fila[4], "").append(ElmentoDeFila)
Resultado = [(key,min(ListaDeValoresPorLetra[key]),max(ListaDeValoresPorLetra[key]))for key  in ListaDeValoresPorLetra]
for item in Resultado:
    print(item[0]+","+str(item[1])+","+str(item[2]))
##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##

import re
import operator

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
CadenasTresLetras = [ (Registro[4])  for Registro in ArchivoEnMemoria]
LetrasUnicas = set(Registro for Registro in CadenasTresLetras) 
LetraUnicas = [k for k  in LetrasUnicas]
LetraUnicas.sort()
ListaDeValoresPorLetra = {Letra:[] for Letra in LetrasUnicas}
for LetraComprobar in LetrasUnicas:
    for Fila in ArchivoEnMemoria:
        for ElementoEnFila in Fila:
            if  ElementoEnFila == LetraComprobar:
                ListaDeValoresPorLetra.get(LetraComprobar, "").append(ElementoEnFila)
Resultado = [(key,ListaDeValoresPorLetra.get(key).count(key))for key  in ListaDeValoresPorLetra]
Resultado = sorted(Resultado ,key = operator.itemgetter(0))
for item in Resultado:
    print(item[0]+","+str(item[1]))
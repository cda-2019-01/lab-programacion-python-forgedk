##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##

import re
ListaDeArchivos = []
Archivo = open('data.csv', 'r')
PatronDeRemplazoValoresConComa = re.compile(r'(\d),')
ArchivoEnMemoria = (Archivo.readlines())
Archivo.close()
ArchivoEnMemoria = [linea.replace("\t", " ") for linea in ArchivoEnMemoria]
ArchivoEnMemoria = [linea[:-1] for linea in ArchivoEnMemoria]
ArchivoEnMemoria = [PatronDeRemplazoValoresConComa.sub(r"\1 ", linea) for linea in ArchivoEnMemoria]
ArchivoEnMemoria = [linea.split(' ') for linea  in ArchivoEnMemoria]
Resultado = [[Letra[0],len(Letra[3].split(",")),len(Letra[4:])] for Letra in ArchivoEnMemoria]
for item in Resultado:
    print(item[0]+","+str(item[1])+","+str(item[2]))
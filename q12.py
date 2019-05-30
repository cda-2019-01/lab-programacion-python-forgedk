##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##


def Suma(List):
    suma = 0
    for elemento in List:
        suma+= int(elemento)
    return suma
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
LetrasColumna4 = [line[3].split(",") for line in ArchivoEnMemoria]
LetrasColumna4 = [letra  for registro in LetrasColumna4 for letra in registro]
LetrasUnicas = set([Registro for Registro in LetrasColumna4]) 
ListaDeValoresPorLetra = {Letra:[] for Letra in LetrasUnicas}
for Fila in ArchivoEnMemoria:
    for letra in Fila[3].split(","):
        ListaDeValoresPorLetra.get(letra).append(Fila[1]) 
Resultado = [(key,Suma(ListaDeValoresPorLetra.get(key,"")))    for key  in ListaDeValoresPorLetra]
Resultado = sorted(Resultado ,key = operator.itemgetter(0))
for item in Resultado:
    print(item[0]+","+str(item[1]))
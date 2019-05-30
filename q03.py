##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
def Suma(List):
    suma = 0
    for elemento in List:
        suma+= int(elemento)
    return suma
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
Letras = [Registro[0] for Registro in ArchivoEnMemoria]
LetrasUnicas = set([Registro[0] for Registro in ArchivoEnMemoria]) 
LetrasUnicas = sorted(LetrasUnicas)
ListaDeValoresPorLetra = {Letra:[] for Letra in LetrasUnicas}
for Fila in ArchivoEnMemoria:
    ListaDeValoresPorLetra.get(Fila[0], "").append(Fila[1])
Resultado = [(key,Suma(ListaDeValoresPorLetra.get(key,"")))    for key  in ListaDeValoresPorLetra]
for item in Resultado:
    print(item[0]+","+str(item[1]))
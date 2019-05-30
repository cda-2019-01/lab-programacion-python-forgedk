##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
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
ArchivoEnMemoria = [linea[:-1] for linea in ArchivoEnMemoria]
ArchivoEnMemoria = [PatronDeRemplazoValoresConComa.sub(r"\1 ", linea) for linea in ArchivoEnMemoria]
ArchivoEnMemoria = [linea.split(' ') for linea  in ArchivoEnMemoria]
ListaDeLetraYRegistros = [[Registro[0] ,Registro[4:]] for Registro in ArchivoEnMemoria]
ListaDeClaveConSuma = []
for Registro in ListaDeLetraYRegistros:
    ListaDeNumeros = []
    for IdentificadorYNumero in Registro[1]:
        ListaDeNumeros.append(IdentificadorYNumero.split(":")[1])
    ListaDeClaveConSuma.append([Registro[0],Suma(ListaDeNumeros)])
for Registro in ListaDeClaveConSuma :
    print(Registro[0]+ ","+ str(Registro[1]))
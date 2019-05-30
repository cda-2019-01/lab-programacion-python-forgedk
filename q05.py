##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
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
Letras = [Registro[0] for Registro in ArchivoEnMemoria]
LetrasUnicas = set([Registro[0] for Registro in ArchivoEnMemoria]) 
LetrasUnicas = sorted(LetrasUnicas)
ListaDeValoresPorLetra = {Letra:[] for Letra in LetrasUnicas}
for Fila in ArchivoEnMemoria:
    ListaDeValoresPorLetra.get(Fila[0], "").append(Fila[1])
Resultado = [(key,max(ListaDeValoresPorLetra[key]),min(ListaDeValoresPorLetra[key]))for key  in ListaDeValoresPorLetra]
for item in Resultado:
    print(item[0]+","+str(item[1])+","+str(item[2]))
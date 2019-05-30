##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
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
ValorSegundaColumna = [Registro[1] for Registro in ArchivoEnMemoria]
ValoresUnicos = set([Registro for Registro in ValorSegundaColumna]) 
ListaDeValoresPorRegistro = {Valor:[] for Valor in ValoresUnicos}
for Fila in ArchivoEnMemoria:
    ListaDeValoresPorRegistro.get(Fila[1], "").append(Fila[0])
for Lista in ListaDeValoresPorRegistro:
     ListaDeValoresPorRegistro.get(Lista).sort()
Resultado = [(key,ListaDeValoresPorRegistro[key])for key  in ListaDeValoresPorRegistro]
Resultado =  sorted(Resultado)
for item in Resultado:
    print("("+"'"+item[0]+"'"+", "+str(item[1])+")")
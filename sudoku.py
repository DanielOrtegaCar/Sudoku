import random
import math as m
from copy import deepcopy
from beautifultable import BeautifulTable

numero_columnas, numero_filas = 9, 9

caja = { 0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, }
aleatorios = []

class Nodo_tablero:

    def __init__(self, numero=0, creado=True, arcos=[], dominios= None):
        self.numero = numero
        self.creado = creado
        self.arcos = arcos
        self.dominios = dominios

class sudoku:

    def __init__(self):
        self.tablero = []
        for i in range(numero_filas * numero_columnas):
            nodo = Nodo_tablero(dominios= [1, 2, 3, 4, 5, 6, 7, 8, 9])
            self.tablero.append(nodo)
        self.rellenar()
        self.generar_arcos(False)

    def generar_arcos(self, prueba=False):
        for i in range(81):
            numero = i
            arcos = []
            arcos = self.limitescol(
                i) + self.limitesfila(i) + self.limitescuadros(i)
            arcos = sorted(set(arcos))
            self.tablero[i].arcos = arcos


    def contar_dominios(self):
        total = 0
        for i in range(81):
            if self.tablero[i].dominios:
            	total = total + len(self.tablero[i].dominios)
        return total

    def imprime(self):
        table = BeautifulTable()
        contador = 0
        for j in range(numero_filas):
            filas = []
            for i in range(numero_columnas):
                filas.append(self.tablero[contador].numero)
                contador += 1
            table.append_row(filas)
        print(table)

    def dominios(self):
        for i in range(81):
            print("i: ",self.tablero[i].dominios)

    def arcos(self):
        for i in range(81):
            print("i: ",self.tablero[i].arcos)

    def rellenar(self):
        arellenar = random.randint(30, 32)
        asignados = 0
        while(asignados != arellenar):
            indice = random.randint(0, 80)
            aleatorio = random.randint(1, 9)
            aux = True
            for j in self.limitesfila(indice):
                if self.tablero[j].numero == aleatorio:
                    aux = False
                    break
            if(aux):
                for j in self.limitescol(indice):
                    if self.tablero[j].numero == aleatorio:
                        aux = False
                        break
            if(aux):
                for j in self.limitescuadros(indice):
                    if self.tablero[j].numero == aleatorio:
                        aux = False
                        break
            if(aux):
                aleatorios.append(aleatorio)
                self.tablero[indice].numero = aleatorio
                self.tablero[indice].creado = False
                self.tablero[indice].dominios=[aleatorio]
                asignados = asignados + 1

    def limitesfila(self, numero):
        residuo = numero % 9
        inicio = numero - residuo
        final = inicio + 9
        numeros = []
        for i in range(inicio, final):
            numeros.append(i)
        numeros.remove(numero)
        return numeros

    def limitescol(self, numero):
        contador = 0
        inicio = numero % 9
        numeros = []
        numeros.append(inicio)
        for i in range(8):
            inicio = inicio + 9
            numeros.append(inicio)
        numeros.remove(numero)
        return numeros

    def limitescuadros(self, numero):

        fila = caja[numero % 9]
        columna = caja[m.floor(numero / 9)]

        if (columna, fila) == (0, 0):
            inicio = 0
        elif (columna, fila) == (0, 1):
            inicio = 3
        elif (columna, fila) == (0, 2):
            inicio = 6
        elif (columna, fila) == (1, 0):
            inicio = 27
        elif (columna, fila) == (1, 1):
            inicio = 30
        elif (columna, fila) == (1, 2):
            inicio = 33
        elif (columna, fila) == (2, 0):
            inicio = 54
        elif (columna, fila) == (2, 1):
            inicio = 57
        elif (columna, fila) == (2, 2):
            inicio = 60

        arr = [inicio, inicio + 1, inicio + 2]
        for i in [0, 3]:
            for j in [0, 1, 2]:
                arr.append(arr[i + j] + 9)
        arr.remove(numero)
        return arr

    def es_completo(self):
        for i in range(81):
            if self.tablero[i].numero == '*':
                return False
        return True

    def acceder(self, fila, columna):
        fila = -1 + fila
        fila = fila * 9
        columna = columna - 1
        columna = columna
        indice = fila + columna
        return self.tablero[indice]


def ac3(tabla):
    cola = []
    for i in range(81):
        for j in tabla.tablero[i].arcos:
            cola.append((i, j))
    while(cola):
        (i, j) = cola.pop()
        if(revise(tabla, i, j)):
            for z in tabla.tablero[i].arcos:
                if i != z:
                    cola.append((z, i))
    return True

# acutaliza el dominio de la variable
def revise(tabla, i, j):
	revisado = False
	for x in tabla.tablero[i].dominios:
		if (len(tabla.tablero[j].dominios) == 1 and x in tabla.tablero[j].dominios):
			tabla.tablero[i].dominios.remove(x)
			revisado=True
	return revisado


'''
def backtrack(indice=0,tabla):
    if indice==81:
        return tabla.imprimir()
    # posicion asignada    
    elif tabla.tablero[indice]!=0:
        backtrack(indice+1,tabla)
    else:
        banderin=True
        for i in tabla.tablero[indice].arcos:
            if i.numero ==asignacion:
                banderin=False
'''

'''
def backtrack(indice=0,tabla):
    if indice==81:
        return tabla.imprimir()
    elif tabla.tablero[indice]!=0:
        backtrack(indice+1,tabla)
    tabla.tablero[indice].numero=tabla.tablero[indice].dominios[0]    
'''



instancia = sudoku()
instancia.imprime()
ac3(instancia)
instancia.dominios()



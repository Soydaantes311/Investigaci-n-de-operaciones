import time
import random

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

lista = list(range(1000))
objetivo = random.randint(0, 999999)

inicio = time.time()
resultado = busqueda_lineal(lista, objetivo)
fin = time.time()

print(f"Objetivo encontrado en el índice: {resultado}")
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

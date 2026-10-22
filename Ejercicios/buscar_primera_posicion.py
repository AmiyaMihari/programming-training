#Devuelve posición donde aparece por primera vez el objetivo

def buscar_primera_posicion(lista_enteros, objetivo):
    i = 0
    while i != len(lista_enteros):
        if lista_enteros[i] == objetivo:
            return i
        i+=1
    return -1

lista = [4, 8, 5, 10]
objetivo = 8
print("Lista 1: ", buscar_primera_posicion(lista, objetivo))

lista = [4, 8, 5, 10]
objetivo = 99
print("Lista 2: ", buscar_primera_posicion(lista, objetivo))


lista = []
objetivo = 0
print("Lista 3: ", buscar_primera_posicion(lista, objetivo))


lista = [2, 5, 2, 3, 5]
objetivo = 5
print("Lista 4: ", buscar_primera_posicion(lista, objetivo))
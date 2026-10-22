#Cuenta cantidad de números positivos en una lista

def sumar_positivos(lista_enteros):
    i = 0
    suma = 0
    while i != len(lista_enteros):
        if lista_enteros[i] > 0:
            suma += lista_enteros[i]
        i+=1
    return suma


print("Lista 1: ", sumar_positivos([4, -2, 0, 7, -5]))

print("Lista 2: ", sumar_positivos([-4, 0, -1]))

print("Lista 2: ", sumar_positivos([]))
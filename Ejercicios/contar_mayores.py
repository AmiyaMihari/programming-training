#Cuenta números mayores a un límite

def contar_mayores(lista_enteros,limite):
    num_mayores = 0
    i = 0
    while i != len(lista_enteros):
        if lista_enteros[i] > limite:
            num_mayores += 1
        i+=1
    return num_mayores

lista = [4, 8, 5, 10]
limite = 5
print("Lista 1: ", contar_mayores(lista, limite))


lista = [12, 23, -23, 12.0000001]
limite = 12
print("Lista 2: ", contar_mayores(lista, limite))


lista = []
limite = 0
print("Lista 3: ", contar_mayores(lista, limite))
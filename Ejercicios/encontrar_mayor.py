#Encontrar número mayor en una lista de enteros. Si está vacía devolver None.

def encontrar_mayor(lista_enteros):
    if len(lista_enteros) == 0:
        return None
    num_mayor = lista_enteros[0]
    i = 1
    while i != len(lista_enteros):
        if lista_enteros[i] > num_mayor:
            num_mayor = lista_enteros[i]
        i+=1
    return num_mayor

lista = [4, 8, 5, 10, 42, 23, 41]
print("Lista 1: ", encontrar_mayor(lista))

lista = []
print("Lista 1: ", encontrar_mayor(lista))


lista = [0]
print("Lista 1: ", encontrar_mayor(lista))

lista = [7]
print("Lista 1: ", encontrar_mayor(lista))

lista = [-1, -2, -10]
print("Lista 1: ", encontrar_mayor(lista))
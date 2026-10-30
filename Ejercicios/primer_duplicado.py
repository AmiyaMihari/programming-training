# Devuelve el número duplicado si algún número aparece más de una vez
# None si no hay duplicado
# Conjuntos ver.

def primer_duplicado(lista_enteros):
    i = 0
    conjunto_enteros = set()
    while i != len(lista_enteros):
        if lista_enteros[i] in conjunto_enteros:
            return lista_enteros[i]
        conjunto_enteros.add(lista_enteros[i])
        i+=1
    return None

lista_enteros = [4, 2, 7, 2]
print(lista_enteros)
print("Duplicado: ", primer_duplicado(lista_enteros))

lista_enteros = [4, 2, 7]
print(lista_enteros)
print("Duplicado: ", primer_duplicado(lista_enteros))

lista_enteros = []
print(lista_enteros)
print("Duplicado: ", primer_duplicado(lista_enteros))

lista_enteros = [5, 4, 3, 2, 1, 1]
print(lista_enteros)
print("Duplicado: ", primer_duplicado(lista_enteros))

lista_enteros = [0, 0]
print(lista_enteros)
print("Duplicado: ", primer_duplicado(lista_enteros))
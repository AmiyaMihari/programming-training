# Devuelve True si algún número aparece más de una vez
# False si todos distintos
# Conjuntos ver.

def tiene_duplicados(lista_enteros):
    if len(lista_enteros) == 0 or len(lista_enteros) == 1:
        return(False)
    i = 0
    conjunto_enteros = set()
    while i != len(lista_enteros):
        if lista_enteros[i] in conjunto_enteros:
            return True
        conjunto_enteros.add(lista_enteros[i])
        i+=1
    return False

lista_enteros = [4, 2, 7, 2]
print(lista_enteros)
print("Duplicado: ", tiene_duplicados(lista_enteros))

lista_enteros = [4, 2, 7]
print(lista_enteros)
print("Duplicado: ", tiene_duplicados(lista_enteros))

lista_enteros = []
print(lista_enteros)
print("Duplicado: ", tiene_duplicados(lista_enteros))


lista_enteros = [5, 4, 3, 2, 1, 1]
print(lista_enteros)
print("Duplicado: ", tiene_duplicados(lista_enteros))
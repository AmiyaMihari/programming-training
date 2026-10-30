# Devuelve True si algún número aparece más de una vez
# False si todos distintos

def tiene_duplicados(lista_enteros):
    if len(lista_enteros) == 0 or len(lista_enteros) == 1:
        return(False)
    i = 0
    while i != len(lista_enteros):
        j = i + 1
        while j != len(lista_enteros):
            if lista_enteros[i] == lista_enteros[j]:
                return True
            j+=1
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
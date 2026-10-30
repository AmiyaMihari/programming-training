# Devuelve el primer núm de la lista que aparece una sola vez

def contar_frecuencias(lista_enteros):
    i=0
    frecuencias = {}

    while i != len(lista_enteros):
        numero = lista_enteros[i]
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1
        i+=1
    return frecuencias

def primer_no_repetido(lista_enteros):
    frecuencias = contar_frecuencias(lista_enteros)
    i=0

    while i != len(lista_enteros):
        if frecuencias[lista_enteros[i]] == 1:
            return lista_enteros[i]
        i+=1
    return None


lista_enteros = [4, 2, 4, 7, 2, 4]
print(lista_enteros)
print("Primer no repetido ", primer_no_repetido(lista_enteros))

lista_enteros = []
print(lista_enteros)
print("Primer no repetido ", primer_no_repetido(lista_enteros))

lista_enteros = [5]
print(lista_enteros)
print("Primer no repetido ", primer_no_repetido(lista_enteros))

lista_enteros = [0, -2, 0, -2, -2]
print(lista_enteros)
print("Primer no repetido ", primer_no_repetido(lista_enteros))
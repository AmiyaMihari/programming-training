# Cuenta cuantas veces aparece un número en una lista

# Función con ciclo While
# def contar_frecuencias(lista_enteros):
#     i=0
#     frecuencias = {}

#     while i != len(lista_enteros):
#         numero = lista_enteros[i]
#         if numero in frecuencias:
#             frecuencias[numero] += 1
#         else:
#             frecuencias[numero] = 1
#         i+=1
#     return frecuencias

# Función con ciclo for
def contar_frecuencias(lista_enteros):
    frecuencias = {}
    for numero in lista_enteros:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1
    return frecuencias


lista_enteros = [4, 2, 4, 7, 2, 4]
print(lista_enteros)
print("Frecuencias ", contar_frecuencias(lista_enteros))

lista_enteros = []
print(lista_enteros)
print("Frecuencias ", contar_frecuencias(lista_enteros))

lista_enteros = [5]
print(lista_enteros)
print("Frecuencias ", contar_frecuencias(lista_enteros))

lista_enteros = [0, -2, 0, -2, -2]
print(lista_enteros)
print("Frecuencias ", contar_frecuencias(lista_enteros))
#Cuenta cantidad de números pares en una lista

def contar_pares(lista_numeros):
    num_pares = 0
    i = 0
    while i != len(lista_numeros):
        num = lista_numeros[i] % 2
        if num == 0:
            num_pares+=1
        i+=1
    return num_pares


print("Lista 1: ", contar_pares([3, 8, 2, 7, 4]))

print("Lista 2: ",contar_pares([]))

print("Lista 3: ",contar_pares([0, -2, -3, 6]))
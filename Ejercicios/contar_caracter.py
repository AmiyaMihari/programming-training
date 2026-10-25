#Devolver cuántas veces aparece un caracter en un texto.

def contar_caracter(texto, objetivo):
    i = 0
    contador = 0
    while i != len(texto):
        if texto[i] == objetivo:
            contador += 1
        i+=1
    return contador


texto = "banana"
objetivo = "a"
print("Texto: ", texto, "\nLetra: ", objetivo)
print("Resultado: ", contar_caracter(texto, objetivo),"\n")

texto = ""
objetivo = "a"
print("Texto: ", texto, "\nLetra: ", objetivo)
print("Resultado: ", contar_caracter(texto, objetivo),"\n")

texto = "CaMAleona"
objetivo = "a"
print("Texto: ", texto, "\nLetra: ", objetivo)
print("Resultado: ", contar_caracter(texto, objetivo),"\n")
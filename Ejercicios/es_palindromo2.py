#Invertir un texto

def es_palindromo(texto):
    i = 0
    j = len(texto) - 1
    while i < j:
        if texto[i] == texto[j]:
            i+=1
            j-=1
        else:
            return False
    return True


texto = "abba"
print("Texto: ", texto)
print("Resultado: ", es_palindromo(texto),"\n")

texto = "oso"
print("Texto: ", texto)
print("Resultado: ", es_palindromo(texto),"\n")

texto = ""
print("Texto: ", texto)
print("Resultado: ", es_palindromo(texto),"\n")

texto = "Oso"
print("Texto: ", texto)
print("Resultado: ", es_palindromo(texto),"\n")

texto = "abca"
print("Texto: ", texto)
print("Resultado: ", es_palindromo(texto),"\n")
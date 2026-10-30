#Invertir un texto

def invertir_texto(texto):
    i = len(texto) - 1
    lista_inv = []
    while i != -1:
        lista_inv.append(texto[i])
        i-=1
    texto_inv = "".join(lista_inv)
    return texto_inv

def es_palindromo(texto):
    texto_inv = invertir_texto(texto)
    if texto == texto_inv:
        return True
    else:
        return False


texto = "banana"
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

texto = "a"
print("Texto: ", texto)
print("Resultado: ", es_palindromo(texto),"\n")
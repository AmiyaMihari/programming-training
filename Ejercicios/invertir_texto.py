#Invertir un texto

def invertir_texto(texto):
    i = len(texto) - 1
    lista_inv = []
    while i != -1:
        lista_inv.append(texto[i])
        i-=1
    texto_inv = "".join(lista_inv)
    return texto_inv


texto = "banana"
print("Texto: ", texto)
print("Resultado: ", invertir_texto(texto),"\n")

texto = ""
print("Texto: ", texto)
print("Resultado: ", invertir_texto(texto),"\n")

texto = "a"
print("Texto: ", texto)
print("Resultado: ", invertir_texto(texto),"\n")

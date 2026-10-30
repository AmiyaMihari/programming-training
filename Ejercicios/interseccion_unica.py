# Lista (en el orden de la lista a) valores en común de la lista_a y lista_b
# En este caso, tiempo adicional es O(n+m2) y Espacio ad. O(m+n)

def interseccion_unica(lista_a, lista_b):
    i=0
    lista_unica = set()
    lista_ordenada = []
    while i != len(lista_b):
      numero = lista_b[i]
      if numero not in lista_unica:
         lista_unica.add(numero)
      i+=1
    
    i=0
    while i != len(lista_a):
      numero = lista_a[i]
      if numero in lista_unica:
          if numero not in lista_ordenada:
             lista_ordenada.append(numero)
      i+=1
    return lista_ordenada


lista_a = [4, 2, 4, 7, 9]
lista_b = [9, 4, 4, 8]

print("Lista_a: ", lista_a)
print("Lista_b: ", lista_b)
print("Resultado: ", interseccion_unica(lista_a, lista_b))

lista_a = [1,2,3,4,5,6,7,8,9]
lista_b = [9,8,7,6,55,44,33,22,11,0]

print("Lista_a: ", lista_a)
print("Lista_b: ", lista_b)
print("Resultado: ", interseccion_unica(lista_a, lista_b))

lista_a = []
lista_b = []

print("Lista_a: ", lista_a)
print("Lista_b: ", lista_b)
print("Resultado: ", interseccion_unica(lista_a, lista_b))
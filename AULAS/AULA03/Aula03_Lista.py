import random
from random import randint

text1 = "Blablabla"

lista1 = list(text1)  # Converte a string em uma lista de caracteres
print(lista1)

print("Lista de numeros")

lista2 = list(range(0,20))
print(lista2)

print("Lista aleatoria")
lista3 = [random.randint(1,10) for i in range(0,20)]
print(lista3)

listaA = lista3[0:3]
print("Lista A: ", listaA)
listaB = lista3[0:20:2]
print("Lista B: ", listaB)
listaC = lista3[::-1]
print("Lista C: ", listaC)

dicionario_executivo = {"faturamento":1000,"funcionários":50,"salario miniumo":1300, "salario maximo":15000, "impostos":300}
print(dicionario_executivo)
print(dicionario_executivo.keys())
print(dicionario_executivo.values())
print(dicionario_executivo.items())
print(dicionario_executivo["fucionarios"])




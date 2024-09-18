'''11. Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
a) o número digitado ao quadrado;
b) o número digitado ao cubo;
c) a raiz quadrada do número digitado;
d) a raiz cúbica do número digitado'''

import math

numero = int(input("Informe um número inteiro e positivo: "))

quadrado = numero ** 2
cubo = numero ** 3

raiz_quadrada = math.sqrt(numero)
raiz_cubica = numero ** (1/3)

print(f"O {numero} ao quadrado é: {quadrado}")
print(f"O {numero} ao cubo é: {cubo}")
print(f"A Raiz qudrada do {numero}é: {raiz_quadrada}")
print(f"A Raiz Cubica ao {numero} é: {raiz_cubica}")


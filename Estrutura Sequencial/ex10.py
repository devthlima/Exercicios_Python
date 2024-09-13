'''
Faça um programa que calcule e mostre a área de um círculo. Sabe-se que: Área = p * R2
.
Solução:
ALGORITMO
DECLARE area, raio NUMÉRICO
LEIA raio
area ← 3.1415 * raio
ESCREVA area
FIM_ALGORITMO
'''
import math

raio = float(input("Informe o raio do círculo: "))

area = math.pi * (raio ** 2)

print("Área do círculo: ",area)
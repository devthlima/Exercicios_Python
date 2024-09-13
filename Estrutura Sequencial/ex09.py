'''
Faça um programa que calcule e mostre a área de um triângulo. Sabe-se que: Área = (base * altura)/2.
Solução:
ALGORITMO
DECLARE base, altura, area NUMÉRICO
LEIA base, altura
area ← (base * altura)/2
ESCREVA area
FIM_ALGORITMO.
'''

base = int(input("Informe o valor da base do triâgulo: "))
altura = int(input("Informe o valor da altura do triângulo: "))

area = (base * altura)/2

print("Área do triângulo: ",area)
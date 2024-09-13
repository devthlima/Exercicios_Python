'''
4. Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se
que este sofreu um aumento de 25%.

1a solução:
ALGORITMO
DECLARE sal, novosal NUMÉRICO
LEIA sal
novosal ← sal + sal * 25/100
ESCREVA novosal
FIM_ALGORITMO.

2a solução:
ALGORITMO
DECLARE sal, aumento, novosal NUMÉRICO
LEIA sal
aumento ← sal * 25/100
novosal ← sal + aumento
ESCREVA novosal
FIM_ALGORITMO.

'''

salario = float(input("Informe seu salário: "))

novo_salario = salario + salario * (25/100)

print("Novo Salário: ",novo_salario)
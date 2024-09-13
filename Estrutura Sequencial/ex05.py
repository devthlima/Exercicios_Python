'''
5. Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre
o valor do aumento e o novo salário.
Solução:
ALGORITMO
DECLARE sal, perc, aumento, novosal NUMÉRICO
LEIA sal, perc
aumento ← sal * perc/100
ESCREVA aumento
novosal ← sal + aumento
ESCREVA novos
'''

salario = float(input("Informe o seu salário: "))
percentual = int(input("Informe a porcentagem do aumento: "))

aumento = salario * (percentual/100)

print("Aumento: ",aumento)

novo_salario = salario + aumento
print("Novo Salario: ",novo_salario)

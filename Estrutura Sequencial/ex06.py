'''
Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber,
sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% também sobre o salário base.
Solução:
ALGORITMO
DECLARE sal, salreceber, grat, imp NUMÉRICO
LEIA sal
grat ← sal * 5/100
imp ← sal * 7/100
salreceber ← sal + grat − imp
ESCREVA salreceber
FIM_ALGORITMO.
'''

salario = float(input("Informe seu salário: "))

graticacao = salario * (5/100)
imposto = salario * (7/100)
salario_receber = salario + graticacao - imposto

print("Salario a raceber: ", salario_receber)


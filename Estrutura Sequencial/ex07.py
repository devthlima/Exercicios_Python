'''
Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber,
sabendo-se que o funcionário tem gratificação de R$ 50 e paga imposto de 10% sobre o salário base.
Solução:
ALGORITMO
DECLARE sal, salreceber, imp NUMÉRICO
LEIA sal
imp ← sal * 10/100
salreceber ← sal + 50 − imp
ESCREVA salreceber
FIM_ALGORITMO.
'''
salario = float(input("Informe seu salario: "))

imposto = salario * (10/100)
salario_receber = salario + 50 - imposto

print("Salario a receber: ",salario_receber)
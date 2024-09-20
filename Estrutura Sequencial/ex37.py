'''
Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário, calcule
e mostre a quantidade de salários mínimos que esse funcionário ganha.
'''

salario_minimo = 1412 
salario_funcionario = float(input("Digite o valor do salário do funcionário: "))
quantidade_salarios = salario_funcionario / salario_minimo

print(f"O funcionário recebe {quantidade_salarios} salários mínimos.")
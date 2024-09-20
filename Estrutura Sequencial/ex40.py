'''
João recebeu seu salário e precisa pagar duas contas atrasadas. Em razão do atraso, ele deverá pagar multa de 2% sobre cada conta. Faça um programa que calcule e mostre quanto restará do salário de João.
'''

salario = float(input("Informe o valor do seu salário: "))

conta_luz = float(input("Informe o valor da conta de luz: "))
conta_agua = float(input("Informe o valor da conta de água: "))

multa = (conta_luz * 0.02) + (conta_agua * 0.02)
restante_salario = salario - (conta_agua + conta_luz + multa)


print(f"Saldo em conta: {restante_salario:.2f}")
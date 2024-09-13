'''
Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o
valor do rendimento e o valor total depois do rendimento.
Solução:
ALGORITMO
DECLARE dep, taxa, rend, total NUMÉRICO

rend ← dep * taxa/100
total ← dep + rend
ESCREVA rend
ESCREVA total
FIM_ALGORITMO.
'''

deposito = float(input("Informe o valor do deposito: "))
taxa = float(input("Informe a taxa de juros: "))

rendimento = deposito * (taxa / 100)
total = deposito + rendimento

print("Rendimento: ",rendimento)
print("Total: ",total)

'''
25. Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo.
Esse programa deverá calcular e mostrar a quantidade de convites que devem ser vendidos para que,
pelo menos, o custo do espetáculo seja alcançado.
Solução:
ALGORITMO
DECLARE custo, convite, qtd NUMÉRICO
LEIA custo
LEIA convite
qtd ← custo / convite
ESCREVA qtd
FIM_ALGORITMO.
'''

custo = float(input("Informe o custo de um espetáculo teatral:"))
convite = float(input("Preço do convite:"))

quantidade = custo / convite

print(f"{quantidade} convites precisam ser vendidos para o custo espetáculos seja alcançado")
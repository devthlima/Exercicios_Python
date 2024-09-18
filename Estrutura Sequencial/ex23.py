'''
23. Faça um programa que receba um número real, encontre e mostre:
a) a parte inteira desse número;
b) a parte fracionária desse número;
c) o arredondamento desse número.
Solução:
ALGORITMO
DECLARE num, i, f, a NUMÉRICO
LEIA num
i ← parte inteira de num
f ← num - i
a ← arredonda (num)
ESCREVA i
ESCREVA f
ESCREVA a
FIM_ALGORITMO.
'''

numero_real = float(input("Informe um número real:"))

# Atribua a parte inteira do número
inteiro = int(numero_real)

# Calcule a parte fracionária
fracionaria = numero_real - inteiro

# Arredonde o número
arredondado = round(numero_real)

# Exiba os resultados
print(f"A parte inteira do número é: {inteiro}")
print(f"A parte fracionária do número é: {fracionaria:.2f}")
print(f"O número arredondado é: {arredondado}")
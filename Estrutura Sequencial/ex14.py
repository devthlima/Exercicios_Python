'''14. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa;
b) quantos anos ela terá em 2050.
Solução:
ALGORITMO
DECLARE ano_atual, ano_nascimento, idade_atual, idade_2050 NUMÉRICO
LEIA ano_atual
LEIA ano_nascimento
idade_atual ← ano_atual − ano_nascimento
idade_2050 ← 2050 − ano_nascimento
ESCREVA idade_atual
ESCREVA idade_2050
FIM_ALGORITMO.'''

ano_nascimento = int(input("Informe o ano de nascimento:"))
ano_atual = int(input("Informe o ano atual:"))

idade_atual = ano_atual - ano_nascimento
idade_2050 = 2050 - ano_nascimento

print("Idade atual:",idade_atual)
print("Em 2050 você terá:",idade_2050)


'''
Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa em anos;
b) a idade dessa pessoa em meses;
c) a idade dessa pessoa em dias;
d) a idade dessa pessoa em semanas.
'''

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_nascimento

idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
idade_semanas = idade_anos * 52

print(f"A idade da pessoa em anos: {idade_anos} anos")
print(f"A idade da pessoa em meses: {idade_meses} meses")
print(f"A idade da pessoa em dias: {idade_dias} dias")
print(f"A idade da pessoa em semanas: {idade_semanas} semanas")
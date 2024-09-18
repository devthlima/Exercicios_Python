'''
12. Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.
Solução:
ALGORITMO
DECLARE num1, num2, r1, r2 NUMÉRICO
LEIA num1, num2
r1 ← num1num2
r2 ← num2num1
ESCREVA r1, r2
FIM_ALGORITMO.
'''

primeiro_numero = int(input("Informe um número maior que zero: "))
segundo_numero = int(input("Informe outro número maior que zero: "))

resultado_um = primeiro_numero ** segundo_numero
resultado_dois = segundo_numero ** primeiro_numero

print(f"{primeiro_numero} elavado a {segundo_numero} é : {resultado_um}")
print(f"{segundo_numero} elavado a {primeiro_numero} é : {resultado_dois}")
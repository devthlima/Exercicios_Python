'''
24. Faça um programa que receba uma hora formada por hora e minutos (um número real), calcule e
mostre a hora digitada apenas em minutos. Lembre-se de que:
- para quatro e meia, deve-se digitar 4.30;
- os minutos vão de 0 a 59.
Solução:
ALGORITMO
DECLARE hora, h, m, conversao NUMÉRICO
LEIA hora
h ← pegar a parte inteira da variável hora
m ← hora - h
conversao ← (h * 60) + (m * 100)
ESCREVA conversao
FIM_ALGORITMO.
'''

hora = float(input("Digite a hora no formato decimal (ex: 4.30): "))

# Pegue a parte inteira (horas)
h = int(hora)
# Calcule os minutos a partir da parte fracionária
m = (hora - h) * 100
# Converta tudo para minutos
conversao = (hora * 60) = m

# Exiba o resultado em minutos
print(f"A hora digitada em minutos é: {conversao:.0f} minutos")
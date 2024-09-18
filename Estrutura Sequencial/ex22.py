'''
22. Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça um programa que receba
o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência. Calcule e
mostre:
a) o valor de cada quilowatt;
b) o valor a ser pago por essa residência;
c) o valor a ser pago com desconto de 15%.

ALGORITMO
DECLARE vlr_sal, qtd_kw, vlr_kw, vlr_reais, desc, vlr_desc NUMÉRICO
LEIA vlr_sal
LEIA qtd_kw
vlr_kw ← vlr_sal / 5
vlr_reais ← vlr_kw * qtd_kw
desc ← vlr_reais * 15 / 100
vlr_desc ← vlr_reais - desc
ESCREVA vlr_kw
ESCREVA vlr_reais
ESCREVA vlr_desc
FIM_ALGORITMO.
'''
valor_salario = float(input("Informe o valor do salário mínimo:"))
quantidade_kw = float(input("Informe a quantidade de quilowatts consumida:"))

# Calcule o valor de cada kilowatt
valor_kw = valor_salario / 5

# Calcule o valor total em reais
valor_reais = valor_kw * quantidade_kw

# Calcule o desconto de 15%
desconto = valor_reais * 15 / 100

# Calcule o valor total com desconto
valor_desconto = valor_reais - desconto

print(f"O valor de cada quilowatt é: R$ {valor_kw}")
print(f"O valor total a ser pago é: R$ {valor_reais}")
print(f"O valor total com desconto de 15% é: R$ {valor_desconto}")
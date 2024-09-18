'''
16. Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, calcule e
mostre o salário a receber, seguindo estas regras:
a) a hora trabalhada vale a metade do salário mínimo.
b) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
c) o imposto equivale a 3% do salário bruto.
d) o salário a receber equivale ao salário bruto menos o imposto.
Solução:
ALGORITMO
DECL ARE horas_t, vlr_sal_min, vlr_hora_t NUMÉRICO
vlr_sal_bru, imp, vlr_sal_liq NUMÉRICO
LEIA horas_t
LEIA vlr_sal_min
vlr_hora_t ← vlr_sal_min / 2
vlr_sal_bru ← vlr_hora_t * horas_t
imp ← vlr_sal_bru * 3 / 100
vlr_sal_liq ← vlr_sal_bru − imp
ESCREVA vlr_sal_liq
FIM_ALGORITMO.
'''

horas_trabalhadas = int(input("Informe a horas trabalhas: "))
valor_salario_minimo = float(input("Informe o valor do salário mínimo: "))

valor_hora_trabalhada = valor_salario_minimo / 2
valor_salario_bruto = valor_hora_trabalhada * horas_trabalhadas
imposto = valor_salario_bruto * 3 / 100
valor_salario_liquido = valor_salario_bruto - imposto

print(f"Valor salário liquido:R$ {valor_salario_liquido}")
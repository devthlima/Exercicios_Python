'''15. O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do
distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica
de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre:
a) o valor correspondente ao lucro do distribuidor;
b) o valor correspondente aos impostos;
c) o preço final do veículo.
Solução:
ALGORITMO
DECLARE p_fab, perc_d, perc_i, vlr_d, vlr_i, p_final NUMÉRICO
LEIA p_fab
LEIA perc_d
LEIA perc_i
vlr_d ← p_fab * perc_d / 100
vlr_i ← p_fab * perc_i / 100
p_final ← p_fab + vlr_d + vlr_i
ESCREVA vlr_d
ESCREVA vlr_i
ESCREVA p_final
FIM_ALGORITMO.'''

preco_fabrica = float(input("Informe o preço de fábrica do veículo:"))
percentual_distribuidor = float(input("Informe o percentual de lucro de distribuidor:"))
percentual_imposto = float(input("Informe o percentual de imposto:"))

valor_distruibuidor = preco_fabrica * percentual_distribuidor / 100
valor_impostos = preco_fabrica * percentual_imposto / 100
preco_final = preco_fabrica + valor_distruibuidor + valor_impostos

print("Valor Correspondente ao Lucro do Distribuidor:",valor_distruibuidor)
print("Valor Correspondente aos impostos:",valor_impostos)
print("Preço Final do Veículo:",valor_impostos)



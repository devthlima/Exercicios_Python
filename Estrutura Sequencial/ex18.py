'''
18. Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais fornece a
quantidade de ração em gramas. A quantidade diária de ração fornecida para cada gato é sempre a
mesma. Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para
cada gato, calcule e mostre quanto restará de ração no saco após cinco dias.
Solução:
ALGORITMO
DECLARE peso_saco, racao_gato1, racao_gato2, total_final NUMÉRICO
LEIA peso_saco
LEIA racao_gato1
LEIA racao_gato2
racao_gato1 ← racao_gato1 / 1000
racao_gato2 ← racao_gato2 / 1000
total_final ← peso_saco − 5 * (racao_gato1 + racao_gato2)
ESCREVA total_final
FIM_ALGORITMO.
'''

peso_saco = float(input("Informe o peso do saco de ração:"))
racao_gato1 = float(input("Informe a quantidade de ração fornecida para o Gato 1:"))
racao_gato2 = float(input("Informe a quantidade de ração fornecida para o Gato 2:"))

racao_gato1 = racao_gato1 / 1000
racao_gato2 = racao_gato2 / 1000

total_final = peso_saco - 5 * (racao_gato1 + racao_gato2)

print(f"Restará {total_final} KG após 5 dias")
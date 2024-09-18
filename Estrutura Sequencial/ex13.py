'''13. Sabe-se que:
pé = 12 polegadas
1 jarda = 3 pés
1 milha = 1,760 jarda
Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.
a) polegadas;
b) jardas;
c) milhas.
Solução:
ALGORITMO
DECLARE pes, polegadas, jardas, milhas NUMÉRICO
LEIA pes
polegadas ← pes * 12
jardas ← pes / 3
milhas ← jardas / 1760
ESCREVA polegadas, jardas, milhas
FIM_ALGORITMO.'''

medida_pes = int(input("Informe uma medida em pés: "))

medida_polegadas = medida_pes * 12
medida_jardas = medida_pes / 3
medida_milhas = medida_jardas / 1760

print(f"A conversão de {medida_pes} pes em Polegadas é: {medida_polegadas}")
print(f"A conversão de {medida_pes} pes em Jardas é: {medida_jardas}")
print(f"A conversão de {medida_pes} pes em Milhas é: {medida_milhas}")
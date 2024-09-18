'''
20. Faça um programa que receba a medida do ângulo (em graus) formado por uma escada apoiada no
chão e encostada na parede e a altura da parede onde está a ponta da escada. Calcule e mostre a medida
dessa escada.
Observação: as funções trigonométricas implementadas nas linguagens de programação trabalham
com medidas de ângulos em radianos.
Solução:
ALGORITMO
DECLARE ang, alt, escada, radiano NUMÉRICO
LEIA ang
LEIA alt
radiano ← ang * 3.14 / 180
escada ← alt / seno(radiano)
ESCREVA escada
FIM_ALGORITMO.
'''
import math 

angulo = int(input("Informe a medida do ângulo em graus:"))
altura = int(input("Informe a altura da parede:"))

radiano = angulo * math.pi / 180
escada = altura / math.sin(radiano)

print(f"O comprimento da escada é: {escada:.2f} metros")


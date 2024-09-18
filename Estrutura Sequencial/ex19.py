'''
19. Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a altura que
o usuário deseja alcançar subindo a escada, calcule e mostre quantos degraus ele deverá subir para
atingir seu objetivo, sem se preocupar com a altura do usuário. Todas as medidas fornecidas devem
estar em metros.
Solução:
ALGORITMO
DECLARE a_degrau, a_usuario, qtd_degraus NUMÉRICO
LEIA a_degrau
LEIA a_usuario
qtd_degraus ← a_usuario / a_degrau
ESCREVA qtd_degraus
FIM_ALGORITMO.
'''
altura_degrau = float(input("Informe a altura do degrau:"))
altura_usuario = float(input("Informe a altura do usuário:"))

quantidade_degraus = altura_usuario / altura_degrau

print("Quantidade de degraus:",quantidade_degraus)

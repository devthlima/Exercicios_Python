'''Faça um programa que calcule e mostre a área de um losango. Sabe-se que: A = (diagonal maior * diagonal menor)/2.'''

diagonal_maior = float(input("Digite o valor da diagonal maior: ")) 
diagonal_menor = float(input("Digite o valor da diagonal menor: "))

area = (diagonal_maior * diagonal_menor)/2

print(f"A área do losango é: {area:.2f}")
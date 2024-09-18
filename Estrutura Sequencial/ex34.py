'''Faça um programa que calcule e mostre a área de um trapézio.
Sabe-se que: A = ((base maior + base menor) * altura)/2'''

base_maior = float(input("Digite o valor da base maior do trapézio: "))
base_menor = float(input("Digite o valor da base menor do trapézio: "))
altura = float(input("Digite o valor da altura do trapézio: "))

area = ((base_maior + base_menor) * altura) / 2

print(f"A área do trapézio é: {area:.2f}")


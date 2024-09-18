'''Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando
peso 2 para a primeira e peso 3 para a segunda.'''

nota1 = float(input("Informe a 1ª Nota:"))
nota2 = float(input("Informe a 2ª Nota:"))

peso1 = 2
peso2 = 3

media_ponderada = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

print(f"A média ponderada das notas é: {media_ponderada:.2f}")
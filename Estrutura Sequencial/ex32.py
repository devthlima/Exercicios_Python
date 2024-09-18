'''
Faça um programa que receba o peso de uma pessoa, calcule e mostre:
a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
b) o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.
'''

peso = float(input("Digite seu peso(em Kg):"))

novo_engordar = peso + (peso * 0.15)
novo_emagrecer = peso - (peso * 0.20)

print(f"Se você engordar 15% do seu peso, irá pesar: {novo_engordar} Kg")
print(f"Se você emagrecer 20% do seu peso, irá pesar: {novo_emagrecer} Kg")
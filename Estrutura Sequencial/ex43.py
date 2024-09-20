'''Faça um programa que receba uma temperatura em Celsius, calcule e mostre essa temperatura em
Fahrenheit. Sabe-se que F = 180*(C + 32)/100.'''

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = 180 * (celsius + 32)/100

print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")
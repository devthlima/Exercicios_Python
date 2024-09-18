'''Faça um programa que receba dois números, calcule e mostre a divisão do primeiro número pelo
segundo. Sabe-se que o segundo número não pode ser zero, portanto, não é necessário se preocupar
com validações.'''

numero_um = int(input("Digite um número: "))
numero_dois = int(input("Digite o segundo número(diferente de zero):)"))

resultado = numero_um / numero_dois 

print(f"{numero_um} dividido por {numero_dois} é:{resultado}")
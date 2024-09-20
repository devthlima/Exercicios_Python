'''
Faça um programa que receba uma hora (uma variável para hora e outra para minutos), calcule e mostre:
a) a hora digitada convertida em minutos;
b) o total dos minutos, ou seja, os minutos digitados mais a conversão anterior;
c) o total dos minutos convertidos em segundos.
'''

hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))

hora_em_minutos = hora * 60

total_minutos = hora_em_minutos + minutos

total_segundos = total_minutos * 60

# Mostra os resultados
print(f"A hora digitada convertida em minutos: {hora_em_minutos} minutos")
print(f"O total dos minutos (hora convertida + minutos digitados): {total_minutos} minutos")
print(f"O total dos minutos convertidos em segundos: {total_segundos} segundos")
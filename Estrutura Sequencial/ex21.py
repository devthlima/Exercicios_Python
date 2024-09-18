'''
21. Uma pessoa deseja pregar um quadro em uma parede. Faça um programa para calcular e mostrar 
a que distância a escada deve estar da parede. A pessoa deve fornecer o tamanho da escada e a altura em
que deseja pregar o quadro.
Lembre-se de que o tamanho da escada deve ser maior que a altura que se deseja alcançar.

Solução:
ALGORITMO
DECLARE X , Y, Z NUMÉRICO
LEIA Z
LEIA X
Y ← Z² - X²
Y ← raiz quadra de Y
ESCREVA Y
FIM_ALGORITMO.

x altura em que deseja pregrar o quadro
y distancia em deverá ficar a escada
z - tamanho da escada
'''
import math

tamanho_escada = int(input("Informe o tamanho da escada:"))
altura_do_quadro = int(input("Informe a altura que o quadro irá ficar:"))

distancia_escada = tamanho_escada ** 2 - altura_do_quadro ** 2

distancia_escada - math.sqrt(distancia_escada)

print(f"A distancia da escada é {distancia_escada:.2f}")
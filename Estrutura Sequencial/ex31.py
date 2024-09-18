'''Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa
que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu
salário final.'''

'''1. Quais são os dados de entrada necessários ? 
2. O que devo fazer fazer com esse dados ? 
3. Quais são as restrições desde problema ? 
4. Qual é o resultado esperado ? 
5. Qual é sequência de passos a ser feitos para chegar ao resultado esperado? '''

#Informe o nome do funcionario
nome_funcionario = input("Digite seu nome: ")

#Informe o salário fixo
salario_fixo = float(input("Digite o salário fixo do funcionário: "))

#Informe o valor da venda
valor_venda = float(input("Digite o valor total das vendas: "))

#calculo da comissão de 4% sobre as vendas
comissao = valor_venda * 0.04

#calculo salário final
salario_final = salario_fixo + comissao

print(f"Comissão: R${comissao:.2f}")
print(f"O salario final do funcionário {nome_funcionario} é: R${salario_final:.2f}")
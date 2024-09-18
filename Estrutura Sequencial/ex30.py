'''Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se
que este sofreu um desconto de 10%.'''


preco_produto = float(input("Informe o valor do produto:"))

desconto = 0.10 * preco_produto

novo_preco = preco_produto - desconto
print(f"O novo preço do produto com 10% de desconto é: R$ {novo_preco:.2f}")
'''
17. Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse trabalhador emitiu dois
cheques e agora deseja saber seu saldo atual. Sabe-se que cada operação bancária de retirada paga
CPMF de 0,38% e o saldo inicial da conta está zerado.
Solução:
ALGORITMO
DECLARE salario, cheque1, cheque2, cpmf1, cpmf2, saldo NUMÉRICO
LEIA salario
LEIA cheque1
LEIA cheque2
cpmf1 ← cheque1 * 0.38 / 100
cpmf2 ← cheque2 * 0.38 / 100
saldo ← salario − cheque1 − cheque2 − cpmf1 − cpmf2
ESCREVA saldo
FIM_ALGORITMO.
'''
print("Seu saldo é: R$ 00")
salario = float(input("Informe o valor do deposito:"))
print(f"Seu saldo agora é: R${salario}")

cheque1 = float(input("Informe o valor do cheque:"))
cheque2 = float(input("Informe o valor do segundo cheque:"))

cpmf1 = cheque1 * 0.38 / 100
cpmf2 = cheque2 * 0.38 / 100
saldo = salario - cheque1 - cheque2 - cpmf1 - cpmf2

print("Valor da conta:R$",saldo)
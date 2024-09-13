nota_um = float(input("Informe a 1ª nota: "))
nota_dois = float(input("Informe a 2ª nota: "))
nota_tres = float(input("Informe a 3ª nota: "))
peso_um = float(input("Informe o peso 1: "))
peso_dois = float(input("Informe o peso 2: "))
peso_tres = float(input("Informe o peso 3: "))

media = (nota_um * peso_dois + nota_dois * peso_dois + nota_tres * peso_tres )/(peso_um + peso_dois + peso_tres)

print("Media",media)
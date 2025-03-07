deposito = float(input("Digite o depósito: "))
taxa = float(input("Digite a taxa: "))

rendimento = deposito * (taxa/100+1)

print (f"O novo valor é {rendimento}.")
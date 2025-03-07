salario = float(input("Digite seu salário: "))

gratificacao = salario * 0.05
imposto = salario * 0.07
novo_salario = salario + gratificacao - imposto

print (f"Sua gratificação é contada em R${gratificacao} e seu imposto em R${imposto}, sendo assim seu salário é R${novo_salario}.")
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))

operador = input("Digite + para somar e - para subtrair: ")[0]
resultado = 0
if (operador == "+"):
    print(f"A soma entre {num1} e {num2} é ",num1+num2)
elif (operador == "-"):
    print(f"A subtração entre {num1} e {num2} é ",num1-num2)
else:
    print("Não foi informado um operador aceito pelo programa!")
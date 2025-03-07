numero = 0
expoente = 0
contador = 1

while (numero <= 0 and expoente <= 0 and expoente <=10):
    numero = float(input("Digite um número maior que 0: "))
    expoente = int(input("Digite o expoente (deve ser maior que 0 e no máximo 10): "))
numero2=numero
while (contador < expoente):
    numero2=numero2*numero
    contador=contador+1
print(f"O resultado é {numero2}.")
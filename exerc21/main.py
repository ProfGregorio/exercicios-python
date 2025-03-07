import math 

a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

if (a != 0 and b != 0 and c != 0):
    delta = b*b -4*a*c
    raiz =  math.sqrt(delta)
    x1 = (-b - raiz)/2*a
    x2 = (-b + raiz)/2*a
    
    if (delta>=0):
        print (f"x1 = {round(x1 , 2)} e x2 = {round(x2, 2)}")
    else:
        print (f"x1 = {round(x1 , 2)}.")
else:
    print ("Operação inválida.")
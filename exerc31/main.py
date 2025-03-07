print("\33[1;35;40mTabuada!\33[m")

numero = int(input("\33[1;35;40mInforme um número: \33[m"))

for i in range(0,10):
     print( numero, "x", i+1, "=", numero * (i+1))
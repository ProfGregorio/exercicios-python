numero = float(input("\33[1;35;40mInforme um número: \33[m"))

unidade = numero % 10
n = (numero - unidade) /10
aux_dezena = n % 10
aux_centena = n 
dezena = aux_dezena
centena = aux_centena

print(centena, "\33[1;35;40mCentena(s)\33[m", dezena, "\33[1;35;40mDezena(s) \33[m", unidade, "\33[1;35;40mUnidade(s)\33[m")
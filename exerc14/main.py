print("\33[1;31;47mAnalise sobre o sexo\33[m\n")

sexo = input("Digite o sexo 'F' para feminino ou 'M' para masculino: ")[0]

if(sexo in 'fF'):
    print("\33[1;35;43mFEMININO\33[m")
elif(sexo in 'mM'):
    print("\33[0;30;41mMASCULINO\33[m")
else:
    print("\33[4;33;44mINVÁLIDO\33[m")

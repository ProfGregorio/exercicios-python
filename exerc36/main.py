print("\33[1;35;40mDias da Semana!\33[m \n")

dias_semanas = ["", "Domingo!", "Segunda-feira!", "Terça-feira!", "Quarta-feira!", "Quinta-feira!", "Sexta-feira!", "Sábado!"]

print("\33[1;35;40mInforme o dia da semana, sendo ele de 1 até 7.\33[m")
dia = int(input("\33[1;37;40mInforme um número:\33[m\n"))

if(dia > 7 or  dia <=0):  
    print("\33[1;31;40mDia da Semana Inválido.\33[m") 
else:
    print(dias_semanas[dia])
print("\33[1;31;40mPeso Ideal.\33[m\n")

print("\33[1;31;40mInformações sobre Gênero.\33[m")
print("\33[1;35;40mPara Feminino: Digite 'F'.\33[m")
print("\33[1;36;40mPara Masculino: Digite 'M'\33[m")

genero = input ("\33[1;31;40mInforme o seu Gênero: \33[m")[0].upper()


if (genero in 'FM'):
    altura = float(input ("\33[1;31;40mInforme a sua altura: \33[m").replace(",", "."))
    if(genero == 'F'):
        print("\33[1;35;40mO seu peso ideal é:\33[m ",round ((62.1 * altura) - 44.7,2),"\33[1;35;40mKg.\33[m")
    else:
        print("\33[1;36;40mO seu peso ideal é:\33[m ",round ((72.7 *altura)- 58,2),"\33[1;36;40mKg.\33[m")
else:
    print("\33[1;31;40mGênero Inválido.\33[m")
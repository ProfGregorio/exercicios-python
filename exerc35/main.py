import math

print("\33[1;35;40mSeja bem-vinda (o) a Loja de Tintas YuZiee! \33[m\n")

area = float(input("\33[1;37;40mInforme o tamanho do local a ser pintado em medros quadrados:\33[m "))

qtd_latas = math.ceil((area/3) /18)

preco = qtd_latas * 80

print("\33[1;35;40mA quantidade de latas usadas é: \33[m", qtd_latas)
print("\33[1;35;40mO valor total será: R$ \33[m",preco)
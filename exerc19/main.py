ordem = []
for n in range(0 , 3):
    ordem.append(int(input("Digite um número: "))) 
ordem.sort(reverse=True)
print(ordem)
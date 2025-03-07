n = 0
consoante = []
palavra = str(input("Digite uma palavra: ").lower())
while(n<len(palavra)):
    if(palavra[n] not in 'aeiou'):
        consoante.append(palavra[n])
    n=n+1
print(consoante)
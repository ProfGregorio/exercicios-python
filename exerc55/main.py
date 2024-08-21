print("*"*100)
print("VERIFICA SE UMA FRASE É PALINDROMO!")
print("*"*100)

def EhPalindromo(frase):
    fraseInvertida = frase[::-1]
    if fraseInvertida == frase:
        return True
    return False

if __name__=='__main__':    
    if(EhPalindromo(input("Digite uma frase:").upper().replace(" ",""))):
        print("A FRASE É UM PALÍNDROMO!")
    else:
        print("A FRASE NÃO É UM PALÍNDROMO!")

num = int(input("Digite um número: "))

def e_primo(n):
    primo = True
    if n <2:
        return False
    else:
        primo = True        
        for i in range(2,n):
            if n%i == 0:
                primo = False
    return primo

for i in range(1,num+1):
    print(i,e_primo(i))
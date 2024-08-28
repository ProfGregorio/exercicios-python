num = int(input("Digite um número: "))

def e_primo(n):
    primo = True

    if n <2:
        return False
    elif n==2:
        primo = True
    else:
        for i in range(3,n):
            if n%i ==0:
                primo = False
                break
            else:
                primo = True
    return primo

for i in range(1,num+1):
    print(i,e_primo(i))
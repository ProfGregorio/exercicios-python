'''
Regras do fizzbuzz
1. Quando a posição é múltipla de 3 fale fizz
2. Quando a posição é múltipla de 5 : fale buzz
3. Quando a posição for múltipla de 3 e 5 fale fizzbuzz
4. Para qualquer outra posição fale o próprio número

Entrada
->Entra um número inteiro

Saída:
-> 
'''
def multiplo_por(n, base):
    return n%base == 0


def fizzbuzzer(pos):    
    if multiplo_por(pos, 3) and multiplo_por(pos, 5):
        return "fizzbuzz"
  
    elif multiplo_por(pos, 3):
        return "fizz"      
    
    elif multiplo_por(pos, 5):
        return "buzz"      
 
    return str(pos)



if __name__ == "__main__":
    assert fizzbuzzer(1) == "1"
    assert fizzbuzzer(2) == "2"
    assert fizzbuzzer(4) == "4"

    assert fizzbuzzer(3) == "fizz"
    assert fizzbuzzer(6) == "fizz"
    assert fizzbuzzer(9) == "fizz"

    assert fizzbuzzer(5) == "buzz"
    assert fizzbuzzer(10) == "buzz"
    assert fizzbuzzer(20) == "buzz"

    assert fizzbuzzer(15) == "fizzbuzz"
    assert fizzbuzzer(30) == "fizzbuzz"
    assert fizzbuzzer(45) == "fizzbuzz"
    assert fizzbuzzer(60) == "fizzbuzz"


    assert fizzbuzzer(19) == "19"
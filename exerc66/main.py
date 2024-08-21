#https://www.w3schools.com/python/ref_string_format.asp
print("*"*100)
print("BOLETIM ACADÊMICO")
print("*"*100)

if __name__=='__main__':    
    desempenho = []
    aluno = []
    qtd_alunos = 0
    notas=0
    while qtd_alunos<4:
        aluno = []
        aluno.append(input("Aluno:"))
        while notas<4:
            aluno.append(float(input(f"Nota {notas+1}:")))
            notas+=1
        aluno.append(sum(aluno[1:])/notas)
        desempenho.append(aluno)        
        notas=0
        qtd_alunos+=1
        print("*"*50)

    print("{:>30}".format("BOLETIM DOS ALUNOS"))
    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Nome", "Nota 1", "Nota 2", "Nota 3", "Nota 4", "Média"))
    print("-"*50)
    for linha in desempenho:
        nome, nota1, nota2, nota3, nota4, media = linha
        print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(nome, nota1, nota2, nota3, nota4, media))
    print("-"*50)
        
desempenho = {}
nomes_materias = ["Português", "Matemática", "Geografia", "História", "Fisíca"]
#Recebe os 10 alunos
for a in range(1,11): #duas entradas para testar
    nome = input(f'Informe o nome do {a}º aluno: ')
    notas_bimestre = {}
    print('-'*70)
    #Recebe as notas das matérias por BIMESTRE
    for b in range (1,5):
        notas = []
        print(f"NOTAS DO {b}º BIMESTRE")

        #Recebe cada nota de cada matéria
        for m in range(5):
            nota = float(input(f'Informe a nota da matéria de {nomes_materias[m]}: '))
            notas.append(nota)
        print('*'*70)
        notas_bimestre[b] = notas
        notas = []
    desempenho[nome] = notas_bimestre

#Calcular a média
for aluno in desempenho:
    medias = []
    for materia in range(5):
        media = 0
        for b in range(1,5):
            media+=desempenho[aluno][b][materia]/4
        medias.append(media)
    desempenho[aluno]["media"] = medias

print(desempenho)


with open("notas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"{desempenho}")
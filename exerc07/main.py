print("Cálculo da média de uma disciplina escolar\n")
disciplina = input("Digite o nome da disciplina: ")

nota1 = int(input("Digite o 1ª nota: "))
nota2 = int(input("Digite o 2ª nota: "))
nota3 = int(input("Digite o 3ª nota: "))
nota4 = int(input("Digite o 4ª nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
condicao = ""

if (media>=7):
    condicao= "Aprovado"
else:
    condicao ="Reprovado"

print(f"O aluno teve as seguintes notas: {nota1}, {nota2}, {nota3}, {nota4} na disciplina de {disciplina} com a média final de {media}.\nSua condição é de {condicao}")




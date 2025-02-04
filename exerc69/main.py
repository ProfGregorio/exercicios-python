import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

times=""
cabecalho = ["Pontos", "Vitórias", "Empates", "Derrotas", "Gols Próprios", "Gols Contras", "Saldo de Gols"]
tabela= dict()
for n in range(0,1):
    desempenho= []
    times=input("Digite o nome do time: ")
    for p in range(0,7):
        info = input(+"     "f"{cabecalho[p]}: ")+"        "
        desempenho.append(info)
    #tabela.update({times:desempenho})
    tabela[times] = desempenho
cls()
print(f"Times {cabecalho}")
for time, d in tabela.items():
    print("  ",time,"  ",d)
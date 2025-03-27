
materias = ["Português", "Matemática", "História", "Física", "Georgrafia"]

class Aluno:
    def __init__(self, nome, sexo, cpf, ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo
        
    def receber_nota():
        pass
    
    def desativar(self):
        self.ativo = False
        print("O aluno foi desativado com sucesso")


class Desempenho(Aluno):
    def __init__(self, materia, bimestre, nota):
        self.materia = materia
        self.bimestre = bimestre
        self.nota = nota


    
if __name__ == "__main__":
    aluno = Aluno("João", "M", "123456", True)
    aluno.desativar()

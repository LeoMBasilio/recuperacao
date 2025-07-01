class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def listar_estudantes(self):
        return self.estudantes

    def calcular_media(self):
        if not self.estudantes:
            return 0
        total = sum(e.nota for e in self.estudantes)
        return total / len(self.estudantes)

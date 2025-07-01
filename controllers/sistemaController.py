from models.turmaModel import Turma
from models.esutdanteModel import Estudante

class SistemaController:
    def __init__(self):
        self.turmas = []

    def criar_turma(self, nome_turma):
        turma = Turma(nome_turma)
        self.turmas.append(turma)

    def obter_turma(self, nome_turma):
        for turma in self.turmas:
            if turma.nome == nome_turma:
                return turma
        return None

    def adicionar_estudante(self, nome_turma, nome_estudante, nota):
        turma = self.obter_turma(nome_turma)
        if not turma:
            return f"Turma '{nome_turma}' não encontrada."
        estudante = Estudante(nome_estudante, nota)
        turma.adicionar_estudante(estudante)
        return "Estudante adicionado com sucesso."

    def listar_estudantes(self, nome_turma):
        turma = self.obter_turma(nome_turma)
        if not turma:
            return None
        return turma.listar_estudantes()

    def listar_todas_turmas(self):
        return self.turmas

    def calcular_media_geral(self):
        total_notas = 0
        total_estudantes = 0
        for turma in self.turmas:
            total_notas += sum(e.nota for e in turma.estudantes)
            total_estudantes += len(turma.estudantes)
        if total_estudantes == 0:
            return 0
        return total_notas / total_estudantes

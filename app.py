from controllers.sistemaController import SistemaController
from views.sistemaView import *

def main():
    controller = SistemaController()

    while True:
        mostrar_menu()
        opcao = solicitar_opcao()

        if opcao == "1":
            nome = solicitar_texto("Nome da turma: ")
            controller.criar_turma(nome)
            mostrar_mensagem("Turma criada.")

        elif opcao == "2":
            turma = solicitar_texto("Nome da turma: ")
            nome = solicitar_texto("Nome do estudante: ")
            nota = solicitar_float("Nota do estudante: ")
            msg = controller.adicionar_estudante(turma, nome, nota)
            mostrar_mensagem(msg)

        elif opcao == "3":
            turma_nome = solicitar_texto("Nome da turma: ")
            estudantes = controller.listar_estudantes(turma_nome)
            if estudantes is None:
                mostrar_mensagem("Turma não encontrada.")
            else:
                mostrar_estudantes(estudantes)

        elif opcao == "4":
            turmas = controller.listar_todas_turmas()
            mostrar_turmas(turmas)

        elif opcao == "5":
            turma_nome = solicitar_texto("Nome da turma: ")
            turma = controller.obter_turma(turma_nome)
            if turma:
                media = turma.calcular_media()
                mostrar_media(media, f"da turma '{turma_nome}'")
            else:
                mostrar_mensagem("Turma não encontrada.")

        elif opcao == "6":
            media_geral = controller.calcular_media_geral()
            mostrar_media(media_geral, "geral")

        elif opcao == "0":
            mostrar_mensagem("Encerrando o programa.")
            break

        else:
            mostrar_mensagem("Opção inválida.")

if __name__ == "__main__":
    main()

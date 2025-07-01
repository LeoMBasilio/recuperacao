def mostrar_menu():
    print("\n--- MENU ---")
    print("[1] Criar nova turma")
    print("[2] Adicionar estudante a uma turma")
    print("[3] Listar estudantes de uma turma")
    print("[4] Listar todas as turmas")
    print("[5] Ver média de uma turma")
    print("[6] Ver média geral")
    print("[0] Sair")

def solicitar_opcao():
    return input("Escolha uma opção: ")

def solicitar_texto(mensagem):
    return input(mensagem)

def solicitar_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número válido.")

def mostrar_mensagem(msg):
    print(msg)

def mostrar_estudantes(estudantes):
    if not estudantes:
        print("Nenhum estudante cadastrado.")
    else:
        for e in estudantes:
            print(f"- {e.nome}: {e.nota}")

def mostrar_turmas(turmas):
    if not turmas:
        print("Nenhuma turma cadastrada.")
    else:
        for t in turmas:
            print(f"- {t.nome} ({len(t.estudantes)} estudantes)")

def mostrar_media(media, contexto=""):
    print(f"Média {contexto}: {media:.2f}")

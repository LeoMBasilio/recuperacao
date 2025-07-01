drive de - https://drive.google.com/drive/folders/18zVtHYgnAbajOPMeaabl6H6tsgJUjt9r
# 📝 Sistema de Cadastro de Estudantes por Turma (Python + MVC)

## 📌 Descrição

Este projeto é um sistema de terminal que permite o **cadastro de estudantes em turmas** com suas respectivas notas, feito em **Python**, utilizando **Programação Orientada a Objetos (POO)** e o **padrão de arquitetura MVC (Model-View-Controller)**.

O sistema permite:
- Criar turmas
- Adicionar estudantes com nota
- Listar estudantes por turma
- Calcular a média das notas por turma
- Calcular a média geral de todas as turmas

---

## 🎯 Objetivos educacionais

- Aplicar **POO com Python** de forma prática
- Utilizar **arquitetura MVC** para separar responsabilidades
- Organizar o código em múltiplos arquivos e pacotes
- Simular uma aplicação real com **entrada/saída via terminal**

---

## 🧱 Conceitos utilizados

### ✅ Programação Orientada a Objetos (POO)

- **Encapsulamento**: cada classe tem seus próprios atributos e métodos.
- **Abstração**: `Estudante` e `Turma` representam entidades reais de forma simplificada.
- **Composição**: uma `Turma` contém uma lista de `Estudantes`.

```python
# model/estudante.py
class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
```

```python
# model/turma.py
class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.estudantes = []
```

### ✅ Padrão MVC

- **Model**: contém as classes `Estudante` e `Turma`.
- **Controller**: regras de negócio no `SistemaController`.
- **View**: mostra informações ao usuário e coleta entradas, sem lógica de decisão.
- **App**: gerencia o fluxo do programa (orquestra tudo).

---

## 🗂️ Estrutura de pastas

```
seu_projeto/
│
├── app.py
├── model/
│   ├── estudante.py
│   └── turma.py
│
├── controller/
│   └── sistema_controller.py
│
└── view/
    └── menu.py
```

---

## ▶️ Como executar

1. Clone ou baixe o repositório
2. Execute:

```bash
python app.py
```

---

## 📋 Exemplo de uso

```
--- MENU ---
[1] Criar nova turma
[2] Adicionar estudante a uma turma
[3] Listar estudantes de uma turma
[4] Listar todas as turmas
[5] Ver média de uma turma
[6] Ver média geral
[0] Sair

Escolha uma opção: 1
Nome da turma: TADS-1
Turma criada.
```

```
Escolha uma opção: 2
Nome da turma: TADS-1
Nome do estudante: Ana
Nota do estudante: 8.5
Estudante adicionado com sucesso.
```

---

## 📌 Responsabilidades por camada

| Camada     | Responsabilidade                                                                 |
|------------|------------------------------------------------------------------------------------|
| Model      | Representar dados (`Estudante`, `Turma`)                                          |
| Controller | Gerenciar lógica de negócio (adicionar, buscar, calcular média, etc)              |
| View       | Mostrar menus, ler entradas, exibir saídas                                        |
| App        | Fazer a ponte entre View e Controller (responsável pelo fluxo do sistema)         |

---

## 🛠 Tecnologias

- Python 3.x
- Terminal / CLI
- Sem bibliotecas externas

---

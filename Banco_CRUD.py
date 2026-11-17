
import sqlite3

# 1. CONEXÃO COM O BANCO DE DADOS

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()


# 2. CRIAÇÃO DA TABELA

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    curso TEXT NOT NULL
)
""")

conexao.commit()


# 3. CREATE - CADASTRAR ALUNO

def cadastrar_aluno():
    print("\n--- CADASTRAR ALUNO ---")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")

    cursor.execute("""
        INSERT INTO alunos (nome, idade, curso)
        VALUES (?, ?, ?)
    """, (nome, idade, curso))

    conexao.commit()

    print("Aluno cadastrado com sucesso!")


# 4. READ - LISTAR ALUNOS

def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")

    cursor.execute("SELECT * FROM alunos")

    alunos = cursor.fetchall()

    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"""
ID: {aluno[0]}
Nome: {aluno[1]}
Idade: {aluno[2]}
Curso: {aluno[3]}
-------------------------
""")


# 5. UPDATE - ATUALIZAR ALUNO

def atualizar_aluno():
    print("\n--- ATUALIZAR ALUNO ---")

    listar_alunos()

    id_aluno = int(input("Digite o ID do aluno: "))

    cursor.execute(
        "SELECT * FROM alunos WHERE id = ?",
        (id_aluno,)
    )

    aluno = cursor.fetchone()

    if aluno is None:
        print("Aluno não encontrado!")
        return

    nome = input("Novo nome: ")
    idade = int(input("Nova idade: "))
    curso = input("Novo curso: ")

    cursor.execute("""
        UPDATE alunos
        SET nome = ?, idade = ?, curso = ?
        WHERE id = ?
    """, (nome, idade, curso, id_aluno))

    conexao.commit()

    print("Aluno atualizado com sucesso!")


# 6. DELETE - EXCLUIR ALUNO

def excluir_aluno():
    print("\n--- EXCLUIR ALUNO ---")

    listar_alunos()

    id_aluno = int(input("Digite o ID do aluno: "))

    cursor.execute(
        "SELECT * FROM alunos WHERE id = ?",
        (id_aluno,)
    )

    aluno = cursor.fetchone()

    if aluno is None:
        print("Aluno não encontrado!")
        return

    confirmacao = input("Deseja realmente excluir? (s/n): ")

    if confirmacao.lower() == "s":
        cursor.execute(
            "DELETE FROM alunos WHERE id = ?",
            (id_aluno,)
        )

        conexao.commit()

        print("Aluno excluído com sucesso!")
    else:
        print("Exclusão cancelada.")


# 7. MENU PRINCIPAL

while True:

    print("""
=================================
       SISTEMA DE ALUNOS
=================================

1 - Cadastrar aluno
2 - Listar alunos
3 - Atualizar aluno
4 - Excluir aluno
0 - Sair

=================================
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        atualizar_aluno()

    elif opcao == "4":
        excluir_aluno()

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")


# 8. ENCERRAR CONEXÃO

conexao.close()

print("Conexão com o banco encerrada.")

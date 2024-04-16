import sqlite3

# Função para criar e popular o banco de dados
def criar_bd():
    # Conectar ao banco de dados
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Criar tabelas
    cursor.execute('''CREATE TABLE IF NOT EXISTS Autores (
                        AutorID INTEGER PRIMARY KEY,
                        Nome TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Editoras (
                        EditoraID INTEGER PRIMARY KEY,
                        Nome TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Livros (
                        LivroID INTEGER PRIMARY KEY,
                        Titulo TEXT,
                        AutorID INTEGER,
                        EditoraID INTEGER,
                        AnoPublicacao INTEGER,
                        FOREIGN KEY (AutorID) REFERENCES Autores(AutorID),
                        FOREIGN KEY (EditoraID) REFERENCES Editoras(EditoraID))''')

    # Inserir dados de exemplo
    cursor.execute("INSERT OR IGNORE INTO Autores (Nome) VALUES ('J.K. Rowling')")
    cursor.execute("INSERT OR IGNORE INTO Autores (Nome) VALUES ('George Orwell')")
    cursor.execute("INSERT OR IGNORE INTO Autores (Nome) VALUES ('Stephen King')")

    cursor.execute("INSERT OR IGNORE INTO Editoras (Nome) VALUES ('Bloomsbury')")
    cursor.execute("INSERT OR IGNORE INTO Editoras (Nome) VALUES ('Penguin Books')")
    cursor.execute("INSERT OR IGNORE INTO Editoras (Nome) VALUES ('Doubleday')")

    cursor.execute("INSERT OR IGNORE INTO Livros (Titulo, AutorID, EditoraID, AnoPublicacao) VALUES ('Harry Potter e a Pedra Filosofal', 1, 1, 1997)")
    cursor.execute("INSERT OR IGNORE INTO Livros (Titulo, AutorID, EditoraID, AnoPublicacao) VALUES ('1984', 2, 2, 1949)")
    cursor.execute("INSERT OR IGNORE INTO Livros (Titulo, AutorID, EditoraID, AnoPublicacao) VALUES ('It', 3, 3, 1986)")

    # Commit e fechar conexão
    conn.commit()
    conn.close()

# Função para recuperar os títulos dos livros
def recuperar_titulos():
    # Conectar ao banco de dados
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Executar a consulta para recuperar os títulos dos livros
    cursor.execute("SELECT Titulo FROM Livros")

    # Recuperar os resultados da consulta
    livros = cursor.fetchall()

    # Imprimir os títulos dos livros
    for livro in livros:
        print(livro[0])

    # Fechar a conexão com o banco de dados
    conn.close()

# Função para recuperar a contagem de livros por autor
def contar_livros_por_autor():
    # Conectar ao banco de dados
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Executar a consulta para contar os livros por autor
    cursor.execute('''SELECT Autores.Nome, COUNT(Livros.LivroID) AS TotalLivros
                      FROM Autores
                      LEFT JOIN Livros ON Autores.AutorID = Livros.AutorID
                      GROUP BY Autores.AutorID''')

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Imprimir os resultados
    for autor, total_livros in resultados:
        print(f"{autor}: {total_livros} livros")

    # Fechar a conexão com o banco de dados
    conn.close()

# Função para recuperar a contagem de livros por editora
def contar_livros_por_editora():
    # Conectar ao banco de dados
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Executar a consulta para contar os livros por editora
    cursor.execute('''SELECT Editoras.Nome, COUNT(Livros.LivroID) AS TotalLivros
                      FROM Editoras
                      LEFT JOIN Livros ON Editoras.EditoraID = Livros.EditoraID
                      GROUP BY Editoras.EditoraID''')

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Imprimir os resultados
    for editora, total_livros in resultados:
        print(f"{editora}: {total_livros} livros")

    # Fechar a conexão com o banco de dados
    conn.close()

# Chamada das funções
criar_bd()
recuperar_titulos()
print("\nContagem de livros por autor:")
contar_livros_por_autor()
print("\nContagem de livros por editora:")
contar_livros_por_editora()

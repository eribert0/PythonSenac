class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
class Livro:
    def __init__(self, titulo, autor_nome, autor_nacionalidade):
        self.titulo = titulo
        self.autor = Autor(autor_nome, autor_nacionalidade)
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
# Criando livros e adicionando à biblioteca
livro1 = Livro(titulo="Dom Casmurro", autor_nome="Machado de Assis", autor_nacionalidade="Brasil")
livro2 = Livro(titulo="Orgulho e Preconceito", autor_nome="Jane Austen", autor_nacionalidade="Reino Unido")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
# Acessando informações dos livros na biblioteca
for livro in biblioteca.livros:
    print(f"Título: {livro.titulo}, Autor: {livro.autor.nome}")
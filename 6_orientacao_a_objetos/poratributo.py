class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)

# Criando autores
autor1 = Autor(nome="Machado de Assis", nacionalidade="Brasil")

autor2 = Autor(nome="Jane Austen", nacionalidade="Reino Unido")

# Criando livros
livro1 = Livro(titulo="Dom Casmurro", autor=autor1)

livro2 = Livro(titulo="Orgulho e Preconceito", autor=autor2)

# Criando biblioteca e adicionando os livros
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

1# Acessando informações dos livros na biblioteca
for livro in biblioteca.livros:
    print(f"Título: {livro.titulo}, Autor: {livro.autor.nome}")
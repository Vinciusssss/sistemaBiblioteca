class Livros:
    def __init__(self):
        self.id = None
        self.status = None
        self.nome = None
        self.autor = None


    def getID(self):
        return self.id
    def getNome(self):
        return self.nome
    def getAutor(self):
        return self.autor
    def getStatus(self):
        return self.status


    def setID(self, id):
        try:
            self.id = int(id)
        except (ValueError, TypeError):
            self.id = None

    def setNome(self, nome):
        if nome and isinstance(nome, str):
            self.nome = nome.strip().title()
        else:
            self.nome = None

    def setAutor(self, autor):
        if autor and isinstance(autor, str):
            self.autor = autor.strip().title()
        else:
            self.autor = None

    def setStatus(self, status):
        if status and isinstance(status, str):
            status_limpo = status.strip().lower()
            if status_limpo == "indisponivel":
                self.status = "indisponivel"
            else:
                self.status = "disponivel"
        else:
            self.status = "disponivel"
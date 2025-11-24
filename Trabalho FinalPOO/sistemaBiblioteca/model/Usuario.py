class Usuario:
    def __init__(self, id, tipo):
        self.id = int(id)
        self.tipo = tipo
        self.nome = None
        self.login = None
        self.idade = 0
        self.senha = None

    def getID(self):
        return self.id
    def getIdade(self):
        return self.idade
    def getLogin(self):
        return self.login
    def getTipo(self):
        return self.tipo
    def getNome(self):
        return self.nome
    def getSenha(self):
        return self.senha

    def setID(self, id):
        try:
            self.id = int(id)
        except (ValueError, TypeError):
            self.id = None

    def setLogin(self, login):
        if login and isinstance(login, str):
            self.login = login.strip()
        else:
            self.login = None

    def setSenha(self, senha):
        if senha and isinstance(senha, str):
            self.senha = senha
        else:
            self.senha = None

    def setTipo(self, tipo):
        if tipo:
            self.tipo = str(tipo).strip()
        else:
            self.tipo = None

    def setNome(self, nome):
        if nome and isinstance(nome, str):
            self.nome = nome.strip().title()
        else:
            self.nome = None

    def setIdade(self, idade):
        try:
            idade_int = int(idade)
            if idade_int > 0:
                self.idade = idade_int
            else:
                self.idade = 0
        except (ValueError, TypeError):
            self.idade = 0
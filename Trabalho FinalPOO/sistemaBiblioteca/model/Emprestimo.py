from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self):
        self.usuario = None
        self.livro = None
        self.dataDeEmprestimo = None
        self.dataDeDevolucao = None

    def getUsuario(self):
        return self.usuario

    def getLivro(self):
        if isinstance(self.livro, str):
            return self.livro
        elif self.livro is not None:
            return self.livro.getNome()
        return None

    def getDataDeEmprestimo(self):
        if self.dataDeEmprestimo:
            return self.dataDeEmprestimo.strftime("%d/%m/%Y")
        return None

    def getDataDeDevolucao(self):
        if self.dataDeDevolucao:
            return self.dataDeDevolucao.strftime("%d/%m/%Y")
        return None

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setLivro(self, livro):
        if hasattr(livro, "getNome"):
            self.livro = livro
        else:
            self.livro = str(livro)

    def setDataDeEmprestimo(self, data=None):
        if data is None:
            self.dataDeEmprestimo = datetime.now()
        else:
            self.dataDeEmprestimo = datetime.strptime(data, "%d/%m/%Y")

    def setDataDeDevolucao(self, data=None):
        if data is None:
            self.dataDeDevolucao = datetime.now() + timedelta(days=7)
        else:
            self.dataDeDevolucao = datetime.strptime(data, "%d/%m/%Y")

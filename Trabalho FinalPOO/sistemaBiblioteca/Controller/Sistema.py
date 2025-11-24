import unicodedata
from random import randint
from model.Livro import Livros
from model.Emprestimo import Emprestimo
from model.Usuario import Usuario
from model.Cliente import Cliente
from model.Bibliotecario import Bibliotecario
from Controller.Mensagem import Mensagem
from sobre.Sobre import Sobre

class Sistema:
    def __init__(self):
        self.usuario_logado = None

    #função principal do sistema
    def start(self):
        while True:
            if self.usuario_logado is None:
                Mensagem.exibirMenuPrincipal(self)
                opcao = input("Digite 1/2/0 : ").upper()
                if opcao not in ["1", "2", "0"]:
                    print("\nOpção inválida! Tente novamente.\n")
                else:
                    if opcao == "1":
                        self.registrarUsuario()
                    elif opcao == "2":
                        tipo_usuario = self.validarLogin()
                        self.executarLogin(tipo_usuario)
                    else:
                        Mensagem.exibirMendsagemSairDoSistema(self)
                        break

            else:
                if self.usuario_logado.getTipo() == "1":
                    Mensagem.exibirTituloMenuBibliotecario(self)
                    while True:
                        self.usuario_logado.menuBibliotecario()
                        escolha = self.usuario_logado.escolhaMenuBibliotecario().upper()
                        if escolha == "1":
                            self.registrarLivro()
                        elif escolha == "2":
                            self.exibirEmprestimos()
                        elif escolha == "3":
                            self.exibirClientes()
                        elif escolha == "4":
                            self.exibirLivros()
                        elif escolha == "5":
                            self.registrarEmprestimo()
                        elif escolha == "6":
                            self.registrarBibliotecario()
                        elif escolha == "7":
                            Mensagem.exibirMensagemSairDoMenuBibliotecario(self)
                            self.usuario_logado = None
                            break

                elif self.usuario_logado.getTipo() == "2":
                    Mensagem.exibirTituloMenuCliente(self)
                    while True:
                        self.usuario_logado.menuCliente()
                        escolha = self.usuario_logado.escolhaMenuCliente().upper()
                        if escolha == "1":
                            self.exibirLivros()
                            Mensagem.exibirTituloListaDeLivros(self)
                        elif escolha == "2":
                            Mensagem.exibirTituloMeusEmprestimos(self)
                            self.exibirMeusEmprestimos()
                        elif escolha == "3":
                            Sobre.mostrarTextoSobreBiblioteca(self)
                        else:
                            Mensagem.exibirMensagemSairDoMenuCliente(self)
                            self.usuario_logado = None
                            break


    def normalizar(self, s):

        if s is None:
            return ""
        s = s.strip()
        s = unicodedata.normalize("NFKD", s)
        s = s.encode("ASCII", "ignore").decode("ASCII")
        return s.strip().upper()

    # funções de login e registro
    def validarLogin(self):
        Mensagem.exibirSelecaoDeTipoDeUsuario(self)
        opcao = input("Selecione o tipo de usuário: ").strip()
        while opcao not in ["1", "2", "0"]:
            print("\nOpção inválida! Digite novamente.\n")
            opcao = input("Digite 1/2/0: ").strip()

        if opcao == "1":
            Mensagem.exibirMensagemExecutandoLoginComoBibliotecario(self)
        elif opcao == "2":
            Mensagem.exibirMensagemExecutandoLoginComoCliente(self)
        else:
            self.start()
        return opcao

    def executarLogin(self, tipo_usuario):
        usuarios_arquivo = self.usuarioFileReader()
        while True:
            userName_inserido = input("UserName (ou 0 para voltar): ").strip()
            if userName_inserido == "0":
                return
            senha_inserida = input("Senha: ").strip()
            usuario_valido = None
            user_input_norm = userName_inserido.strip()
            senha_input_norm = senha_inserida.strip()

            for u in usuarios_arquivo:
                login_arquivo = (u.getLogin() or "").strip()
                senha_arquivo = (u.getSenha() or "").strip()
                tipo_arquivo = str(u.getTipo()).strip()

                if (
                        login_arquivo == user_input_norm and
                        senha_arquivo == senha_input_norm and
                        tipo_arquivo == str(tipo_usuario)
                ):
                    usuario_valido = u
                    break
            if usuario_valido:
                Mensagem.exibirBoasVindasAoUsuario(self, usuario_valido.getNome())
                self.usuario_logado = usuario_valido
                return
            else:
                Mensagem.exibirAvisoDeLoginIncorreto(self)

    def registrarUsuario(self):
        Mensagem.exibirTituloRegistroDeNovoCliente(self)
        nome = input("Digite seu nome (digite 0 para voltar): ").strip()
        if nome == "0":
            self.start()
            return
        login = input("Digite seu login (userName): ").strip()
        senha = input("Digite sua senha: ").strip()

        if not nome or not login or not senha:
            print("\nERRO: Nenhum campo pode ficar vazio!")
            return
        if nome.isdigit() or login.isdigit() or senha.isdigit():
            print("\nERRO: Nome, login e senha não podem ser apenas números!")
            return
        if not any(c.isalpha() for c in nome):
            print("\nERRO: O nome deve conter letras!")
            return

        usuarios_existentes = self.usuarioFileReader()
        for usuario in usuarios_existentes:
            if usuario.getLogin().lower() == login.lower():
                print("\nERRO: Já existe um usuário com esse login!")
                return

        novo_usuario = Cliente(randint(1, 9999), "2")
        novo_usuario.setNome(nome)
        novo_usuario.setLogin(login)
        novo_usuario.setSenha(senha)

        try:
            self.usuarioFileWriter(novo_usuario)
            Mensagem.exibirMensagemDeRegistroConcluido(self)
        except Exception as erro:
            print("\nERRO AO SALVAR O USUÁRIO!")
            print(f"Motivo: {erro}")
            print("O usuário NÃO foi salvo.")

    def registrarBibliotecario(self):
        Mensagem.exibirTituloRegistroDeNovoBibliotecario(self)

        nome = input("Digite seu nome (digite 0 para voltar): ").strip()
        if nome == "0":
            return

        login = input("Digite seu login (userName): ").strip()
        senha = input("Digite sua senha: ").strip()

        if not nome or not login or not senha:
            print("\nERRO: Nenhum campo pode ficar vazio!")
            return
        if nome.isdigit() or login.isdigit() or senha.isdigit():
            print("\nERRO: Nome, login e senha não podem ser apenas números!")
            return
        if not any(c.isalpha() for c in nome):
            print("\nERRO: O nome deve conter letras!")
            return

        bibliotecario_existentes = self.usuarioFileReader()
        for usuario in bibliotecario_existentes:
            if usuario.getLogin().lower() == login.lower():
                print("\nERRO: Já existe um usuario com esse login!")
                return

        novo_usuario = Bibliotecario(randint(1, 9999), "1")
        novo_usuario.setNome(nome)
        novo_usuario.setLogin(login)
        novo_usuario.setSenha(senha)

        try:
            self.usuarioFileWriter(novo_usuario)
            Mensagem.exibirMensagemDeRegistroConcluido(self)
        except Exception as erro:
            print("\nERRO AO SALVAR O USUÁRIO!")
            print(f"Motivo: {erro}")
            print("O usuário NÃO foi salvo.")


    # funções de escrita e leitura de arquivo do usuário
    def usuarioFileWriter(self, novo_usuario):
        try:
            nome_arquivo = "usuariosCadastrados/usuarios.txt"
            texto = (
                f"ID: {novo_usuario.getID()} | "
                f"TIPO: {novo_usuario.getTipo()} | "
                f"NOME: {novo_usuario.getNome()} | "
                f"LOGIN: {novo_usuario.getLogin()} | "
                f"SENHA : {novo_usuario.getSenha()}\n"
            )
            with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
                arquivo.write(texto)
            print(f"\n╔" + "═" * 40 + "╗")
            print(f"║{'Arquivo salvo com sucesso!':^40}║")
            print("╚" + "═" * 40 + "╝")
        except Exception as erro:
            print(f"\n╔" + "═" * 40 + "╗")
            print(f"║{'Erro ao salvar o arquivo do usuário ' + novo_usuario.getLogin():^40}║")
            print("╚" + "═" * 40 + "╝")

    def usuarioFileReader(self):
        caminho = "usuariosCadastrados/usuarios.txt"
        usuarios = []
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    if not linha:
                        continue
                    partes = linha.split("|")
                    info = {}
                    for p in partes:
                        if ":" in p:
                            chave, valor = p.split(":", 1)
                            info[chave.strip()] = valor.strip()

                    if info.get("TIPO") == "1":
                        usuario = Bibliotecario(info["ID"])
                    elif info.get("TIPO") == "2":
                        usuario = Cliente(info["ID"], "2")
                    else:
                        continue
                    usuario.setNome(info.get("NOME"))
                    usuario.setLogin(info.get("LOGIN"))
                    usuario.setSenha(info.get("SENHA"))
                    usuarios.append(usuario)
        except:
            pass
        return usuarios



    def exibirClientes(self):
        lista = self.usuarioFileReader()
        i = 1
        for cliente in lista:
            if cliente.getTipo() == "2":
                print(f"{i} - {cliente.getNome()}")
                i += 1


    # livro
    def registrarLivro(self):
        print("\n--- Registro de Novo Livro ---")
        nome = input("Digite o nome do livro (digite 0 para voltar: )").upper().strip()
        if nome == "0":
            return
        autor = input("Digite o autor: ").upper().strip()

        if not nome:
            print("ERRO: O nome do livro não pode ser vazio!")
            return
        if not autor:
            print("ERRO: O nome do autor não pode ficar vazio!")
            return
        if autor.isdigit():
            print("ERRO: O autor não pode ser apenas números!")
            return

        caminho = "livrosCadastrados/livros.txt"
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip().upper()
                    if not linha:
                        continue

                    partes = linha.split("|")

                    nome_existente = partes[1].split(":")[1].strip()
                    autor_existente = partes[2].split(":")[1].strip()

                    if nome_existente == nome and autor_existente == autor:
                        print("Livro já cadastrado! Registro negado.")
                        return
        except FileNotFoundError:
            pass
        novo_id = randint(1, 9999)
        texto = (
            f"ID:{novo_id} | "
            f"NOME:{nome} | "
            f"AUTOR:{autor} | "
            f"STATUS:DISPONÍVEL\n"
        )
        try:
            with open(caminho, "a", encoding="utf-8") as arquivo:
                arquivo.write(texto)
            print("Novo Livro registrado com sucesso!")
        except Exception as erro:
            print(f"ERRO ao salvar o livro: {erro}")


    def exibirLivros(self):
        lista = self.livroFileReader()
        i = 1
        for livro in lista:
            print(f"{i} - {livro.getNome()} - {livro.getStatus()}")
            i += 1


    def livroFileWriter(self, novoLivro):
        try:
            nome_arquivo = "livrosCadastrados/livros.txt"
            texto = (
                f"ID:{novoLivro.getID()} | "
                f"NOME:{self.normalizar(novoLivro.getNome())} | "
                f"AUTOR:{self.normalizar(novoLivro.getAutor())} | "
                f"STATUS:{self.normalizar(novoLivro.getStatus())}\n"
            )
            with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
                arquivo.write(texto)
            print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")
        except Exception as erro:
            print(f"Erro ao salvar o arquivo do livro {novoLivro.getNome()}: {erro}")


    def livroFileReader(self):
        caminho = "livrosCadastrados/livros.txt"
        lista_Livros = []

        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    if not linha:
                        continue

                    partes = [p.strip() for p in linha.split("|")]
                    info = {}

                    for p in partes:
                        if ":" in p:
                            chave, valor = p.split(":", 1)
                            info[chave.strip().upper()] = valor.strip()

                    livro = Livros()
                    livro.setID(info.get("ID"))
                    livro.setNome(info.get("NOME", ""))
                    livro.setAutor(info.get("AUTOR", ""))
                    livro.setStatus(info.get("STATUS", ""))
                    lista_Livros.append(livro)

        except FileNotFoundError:
            print("Arquivo de livros não encontrado.")
        except Exception as erro:
            print(f"Erro ao ler arquivo de livros: {erro}")

        return lista_Livros


    # emprestimos
    def registrarEmprestimo(self):
        print("\n--- Registro de Novo Empréstimo ---")
        usuario_digitado = input("Digite o nome do usuário (digite 0 para voltar): ").strip()
        if usuario_digitado == "0":
            return
        nome_livro = input("Digite o nome do livro: ").strip().upper()
        lista_usuarios = self.usuarioFileReader()
        lista_livros = self.livroFileReader()
        usuario_encontrado = None
        for usuario in lista_usuarios:
            if self.normalizar(usuario.getNome()) == self.normalizar(usuario_digitado):
                usuario_encontrado = usuario
                break
        if usuario_encontrado is None:
            print("\nUsuário inexistente! Empréstimo negado.")
            return
        livro_encontrado = None
        nome_livro_norm = self.normalizar(nome_livro)
        for livro in lista_livros:
            if self.normalizar(livro.getNome()) == nome_livro_norm:
                livro_encontrado = livro
                break
        if livro_encontrado is None:
            print("\nLivro não encontrado!")
            return
        if self.normalizar(livro_encontrado.getStatus()) == "INDISPONIVEL":
            print("\nEste livro já está emprestado!")
            return
        novoEmprestimo = Emprestimo()
        novoEmprestimo.setUsuario(usuario_encontrado.getNome())
        novoEmprestimo.setLivro(livro_encontrado.getNome())
        novoEmprestimo.setDataDeEmprestimo()
        novoEmprestimo.setDataDeDevolucao()
        self.emprestimoFileWriter(novoEmprestimo)
        livro_encontrado.setStatus("INDISPONIVEL")
        self.livroReWriter(lista_livros)
        print("\nEmpréstimo registrado com sucesso!")



    def emprestimoFileWriter(self, e):
        caminho = "emprestimosCadastrados/emprestimos.txt"

        texto = (
            f"USUARIO:{e.getUsuario()} | "
            f"LIVRO:{e.getLivro().upper()} | "
            f"DATAEMPRESTIMO:{e.getDataDeEmprestimo().upper()} | "
            f"DATADEVOLUCAO:{e.getDataDeDevolucao().upper()}\n"
        )

        with open(caminho, "a", encoding="utf-8") as arquivo:
            arquivo.write(texto)


    def livroReWriter(self, lista_livros):
        caminho = "livrosCadastrados/livros.txt"
        try:
            with open(caminho, "w", encoding="utf-8") as arquivo:
                for livro in lista_livros:
                    texto = (
                        f"ID:{livro.getID()} | "
                        f"NOME:{self.normalizar(livro.getNome())} | "
                        f"AUTOR:{self.normalizar(livro.getAutor())} | "
                        f"STATUS:{self.normalizar(livro.getStatus())}\n"
                    )
                    arquivo.write(texto)
        except Exception as erro:
            print(f"Erro ao atualizar arquivo de livros: {erro}")


    def exibirEmprestimos(self):
        lista = self.emprestimoFileReader()
        i = 1
        for e in lista:
            print(
                f"{i} - LIVRO: {e.getLivro()} / CLIENTE: {e.getUsuario()} / INÍCIO: {e.getDataDeEmprestimo()} / DEVOLUÇÃO: {e.getDataDeDevolucao()}"
            )
            i += 1

    def exibirMeusEmprestimos(self):
        usuario = self.usuario_logado.getNome().strip().upper()
        lista_de_emprestimos = self.emprestimoFileReader()
        i = 1
        for emprestimo in lista_de_emprestimos:
            if emprestimo.getUsuario().strip().upper() == usuario:
                print(
                    f"{i} - LIVRO: {emprestimo.getLivro()} / "
                    f"INÍCIO: {emprestimo.getDataDeEmprestimo()} / "
                    f"DEVOLUÇÃO: {emprestimo.getDataDeDevolucao()}"
                )
                i += 1


    def emprestimoFileReader(self):
        caminho = "emprestimosCadastrados/emprestimos.txt"
        lista = []
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip().upper()
                    if not linha:
                        continue
                    partes = linha.split("|")
                    info = {}
                    for p in partes:
                        if ":" in p:
                            chave, valor = p.split(":", 1)
                            info[chave.strip()] = valor.strip()
                    emp = Emprestimo()
                    emp.setUsuario(info.get("USUARIO"))
                    emp.setLivro(info.get("LIVRO"))
                    emp.setDataDeEmprestimo(info.get("DATAEMPRESTIMO"))
                    emp.setDataDeDevolucao(info.get("DATADEVOLUCAO"))

                    lista.append(emp)
        except FileNotFoundError:
            print("Arquivo de empréstimos não encontrado!")

        return lista
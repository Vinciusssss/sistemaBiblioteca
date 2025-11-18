class Mensagem:
    def exibirMenuPrincipal(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "BIBLIOTECA - MENU PRINCIPAL".center(50) + "║")
        print("╠" + "═" * 50 + "╣")
        print("║" + "1 - Registrar".ljust(50) + "║")
        print("║" + "2 - Entrar".ljust(50) + "║")
        print("║" + "0 - Sair".ljust(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirMendsagemSairDoSistema(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "SAINDO DO SISTEMA...".center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirMensagemExecutandoLoginComoBibliotecario(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "EXECUTANDO LOGIN COMO BIBLIOTECÁRIO".center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirMensagemExecutandoLoginComoCliente(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "EXECUTANDO LOGIN COMO CLIENTE".center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirTituloMenuBibliotecario(self):
        titulo = f"MENU DO BIBLIOTECÁRIO ({self.usuario_logado.getNome()})"
        print("\n╔" + "═" * 50 + "╗")
        print("║" + titulo.center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirMensagemSairDoMenuBibliotecario(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "SAINDO DO MENU DO BIBLIOTECÁRIO...".center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirTituloMenuCliente(self):
        titulo = f"MENU DO CLIENTE ({self.usuario_logado.getNome()})"
        print("\n╔" + "═" * 50 + "╗")
        print("║" + titulo.center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirTituloListaDeLivros(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "LISTA DE LIVROS DISPONÍVEIS".center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirMensagemSairDoMenuCliente(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "SAINDO DO MENU DO CLIENTE...".center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirSelecaoDeTipoDeUsuario(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "SELECIONE O TIPO DE USUÁRIO".center(50) + "║")
        print("╠" + "═" * 50 + "╣")
        print("║" + "1 - Bibliotecário".ljust(50) + "║")
        print("║" + "2 - Cliente".ljust(50) + "║")
        print("║" + "0 - Voltar".ljust(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirAvisoDeLoginIncorreto(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "USERNAME OU SENHA INCORRETOS".center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirBoasVindasAoUsuario(self, usuario):
        mensagem = f"Bem-vindo, {usuario}!"
        print("\n╔" + "═" * 50 + "╗")
        print("║" + mensagem.center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirTituloRegistroDeNovoCliente(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "REGISTRO DE NOVO CLIENTE".center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirTituloRegistroDeNovoBibliotecario(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "REGISTRO DE NOVO BIBLIOTECARIO".center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirMensagemDeRegistroConcluido(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "USUÁRIO REGISTRADO COM SUCESSO!".center(50) + "║")
        print("╚" + "═" * 50 + "╝")

    def exibirTituloMeusEmprestimos(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "MEUS EMPRÉSTIMOS".center(50) + "║")
        print("╚" + "═" * 50 + "╝")
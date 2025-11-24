from model.Usuario import Usuario

class Bibliotecario(Usuario):
    def __init__(self, id, tipo="1"):
        super().__init__(id, tipo)

    def menuBibliotecario(self):
        print("\n╔" + "═" * 45 + "╗")
        print("║" + " MENU DO BIBLIOTECÁRIO ".center(45) + "║")
        print("╠" + "═" * 45 + "╣")
        print("║  1 - Registrar Livro".ljust(46) + "║")
        print("║  2 - Exibir Empréstimos".ljust(46) + "║")
        print("║  3 - Exibir Clientes".ljust(46) + "║")
        print("║  4 - Exibir Livros".ljust(46) + "║")
        print("║  5 - Realizar Empréstimo".ljust(46) + "║")
        print("║  6 - Registrar um novo Bibliotecario".ljust(46) + "║")
        print("║  7 - Sair".ljust(46) + "║")
        print("╚" + "═" * 45 + "╝")

    def escolhaMenuBibliotecario(self):
        escolha = input("Selecione uma opção do Menu Bibliotecário: ")

        while escolha not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("\nOpção inválida! Tente novamente.\n")
            self.menuBibliotecario()
            escolha = input("Selecione uma opção do Menu Bibliotecário: ")

        return escolha
from model.Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, id, tipo):
        super().__init__(id,"2")

    def menuCliente(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + " MENU DO CLIENTE ".center(50) + "║")
        print("╠" + "═" * 50 + "╣")
        print("║  1 - Exibir livros".ljust(51) + "║")
        print("║  2 - Meus Emprestimos".ljust(51) + "║")
        print("║  3 - Sobre".ljust(51) + "║")
        print("║  4 - Sair".ljust(51) + "║")
        print("╚" + "═" * 50 + "╝")

    def escolhaMenuCliente(self):
        escolha = input("Selecione uma opção do Menu Cliente: ")

        while escolha not in ["1", "2", "3", "4"]:
            print("\nOpção inválida! Tente novamente.\n")
            self.menuCliente()
            escolha = input("Selecione uma opção do Menu Cliente: ")

        return escolha



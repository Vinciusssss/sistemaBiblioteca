class Sobre():
    def mostrarTextoSobreBiblioteca(self):
        print("\n╔" + "═" * 50 + "╗")
        print("║" + "SOBRE A BIBLIOTECA".center(50) + "║")
        print("╚" + "═" * 50 + "╝")

        texto1 = (
            "A Atlas Code foi fundada com uma missão clara: ser o pilar de "
            "sustentação para a gestão de dados complexos através de código "
            "elegante e robusto."
        )

        texto2 = (
            "Acreditamos em construir fundações sólidas de software para que nossos "
            "clientes possam navegar seus mapas de informação com total facilidade "
            "e autonomia."
        )

        texto3 = (
            "O Folio é nosso primeiro produto, uma ferramenta que honra essa visão, "
            "trazendo clareza e poder para a gestão de bibliotecas."
        )


        def formatar_texto(t):
            linhas = []
            palavras = t.split()
            linha = ""

            for p in palavras:
                if len(linha) + len(p) + 1 > 50:
                    linhas.append(linha)
                    linha = p
                else:
                    linha += (" " if linha else "") + p
            if linha:
                linhas.append(linha)
            return linhas

        for bloco in (texto1, texto2, texto3):
            linhas = formatar_texto(bloco)
            for linha in linhas:
                print("║" + linha.ljust(50) + "║")
            print("╠" + "─" * 50 + "╣")

        print("╚" + "═" * 50 + "╝")
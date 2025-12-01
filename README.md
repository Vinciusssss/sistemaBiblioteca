📚 #Sistema de Gerenciamento de Biblioteca

Um sistema de biblioteca desenvolvido em Python utilizando os conceitos de Programação Orientada a Objetos (POO). O sistema permite a interação de dois tipos de usuários (Bibliotecário e Cliente) e utiliza persistência de dados em arquivos de texto (.txt) para armazenar usuários, livros e empréstimos.

📋 ##Sobre o Projeto

Este projeto foi desenvolvido como trabalho final da disciplina de Orientação a Objetos. O objetivo principal é simular as operações cotidianas de uma biblioteca, aplicando conceitos como:

Herança (Classes Usuario, Cliente, Bibliotecario).

Encapsulamento.

Manipulação de Arquivos (Leitura e escrita em .txt).

Arquitetura MVC (Separação entre Model, Controller e View/Mensagens).

🚀 ##Funcionalidades

O sistema possui menus dinâmicos baseados no tipo de usuário logado:

👤 ##Cliente

Cadastro: Auto-registro no sistema.

Consultar Acervo: Visualizar livros disponíveis para empréstimo.

Realizar Empréstimo: Alugar livros (com verificação de disponibilidade).

Informações: Visualizar dados sobre a biblioteca.

💼 ##Bibliotecário (Admin)

Gerenciar Acervo: Cadastrar novos livros no sistema.

Relatórios:

Visualizar todos os empréstimos ativos.

Listar todos os clientes cadastrados.

Listar todos os livros (disponíveis e emprestados).

🛠️ ##Tecnologias Utilizadas

Python 3

Manipulação de arquivos (File I/O)

Biblioteca datetime para gestão de datas.

Biblioteca random para geração de IDs.

⚙️ ##Como Executar

Certifique-se de ter o Python 3.x instalado.

Clone este repositório ou baixe os arquivos.

Abra o terminal na pasta raiz do projeto.

Execute o comando:

python main.py


💾 ##Persistência de Dados

O sistema não utiliza banco de dados SQL. Todos os dados são salvos localmente em arquivos .txt formatados com separadores (|), garantindo que as informações não sejam perdidas ao fechar o programa.

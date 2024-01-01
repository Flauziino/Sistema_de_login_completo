Sistema de Login Modularizado
Este é um sistema de login modularizado em Python que utiliza o padrão de projeto Builder (complexidade adicionada apenas para treinamento), separando funcionalidades em módulos para facilitar a manutenção e expansão do sistema.
Nesse projeto foi feito CREATE, READ, UPDATE e DELETE

Estrutura do Projeto

    dados_menu: Módulo para a interface do usuário.
        menu.py: Contém as funções responsáveis pela interação com o usuário.

    registros: Módulo para operações de registros de usuários.
        arquivos_registro.py: Funções para verificar, criar, ler, atualizar e deletar dados de usuários armazenados em arquivos JSON.
        registro.py: Implementação do padrão Builder para a criação de registros de usuários.

    testes: Módulo contendo testes para as funcionalidades do sistema.
        test_dados_menu.py: Testes para as funções de interface.
        test_arquivos_registro.py: Testes para as operações de registros.
        test_registro.py: Testes para a implementação do padrão Builder.

main.py: Arquivo principal contendo a lógica central do programa.

Instalação e Execução
Clone o repositório:

bash
Copy code
git clone https://github.com/Flauziino/Sistema_de_login_completo
Instale as dependências:

bash
Copy code
pip install -r requirements.txt
Execute o sistema:

bash
Copy code
python main.py
Uso
O arquivo main.py contém a lógica principal do sistema. Execute este arquivo para iniciar o programa.

Os diferentes módulos contêm funcionalidades específicas do sistema, como interação com o usuário (dados_menu), operações de registros (registros), implementação do padrão Builder (registro), e testes correspondentes (testes).

Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas abrindo uma issue.
Autores
Flauziino - Desenvolvedor
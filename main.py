from registros import registro, arquivos_registro
from dados_menu import menu
from time import sleep
import os


# MAIN
if __name__ == '__main__':
    usuarios = 'usuarios.json'

    # Logica para verificar a existencia do arquivo
    # Se o arquivo nao existir ira criar
    if not arquivos_registro.verifica_arquivo(usuarios):
        arquivos_registro.cria_arquivo(usuarios)

    # Variavel do menu principal (recebe uma lista de opcoes)
    MENU = [
        '1-Realizar cadastro',
        '2-Realizar login',
        '3-Finalizar'
    ]

    # Variavel do menu apos o login ser bem sucedido
    # Recebe lista de opcoes
    MENU_LOGIN = [
        '1-Editar dados de cadastro',
        '2-Apagar conta',
        '3-Deslogar'
    ]

    # instanciando o builder
    user_builder = registro.UsuarioConstrutor()
    # linkando o builder com diretorio de usuario
    diretorio_usuario = registro.DiretorioUsuario(user_builder)

    sistema_principal = True  # Variavel para manter sistema rodando
    while sistema_principal:
        try:
            menu.titulos('MENU PRINCIPAL')
            menu.menu(MENU)
            opcao = menu.ler_inteiro('Escolha uma opcao>> ')
            os.system('cls')

            # Logica para realizar cadastro
            if opcao == 1:
                # Criaçao do usuario
                # (CREATE)
                menu.titulos('AREA DE CADASTRO')

                nome = str(input('Digite o seu primeiro nome: ')).strip()
                ultimo_nome = str(
                    input('Digite o seu ultimo nome: ')
                )
                email = input('Digite um email: ')
                senha_1 = input('Digite uma senha: ')
                senha_2 = input('Confirme a senha: ')

                # Realizar leitura do JSON para validar se o email
                # ja consta salvo pra outro usuario
                # caso seja um email "novo", permitir o cadastro
                if arquivos_registro.validacao_cadastro(usuarios, email):
                    # Salvando os dados usando diretorio_usuario instanciado
                    user = diretorio_usuario.with_credentials(
                        nome,
                        ultimo_nome,
                        email,
                        senha_1,
                        senha_2
                    )

                    # Pegando os dados de "user" e transformando em um dict
                    # para poder salvar corretamente em jSON
                    user_dict = dict(
                        primeiro_nome=user.primeiro_nome,
                        ultimo_nome=user.ultimo_nome,
                        email=user.email,
                        senha=user.senha
                    )

                    # Salvando os dados de "user_dict" no jSON
                    arquivos_registro.salva_usuario(usuarios, user_dict)
                    menu.titulos('CADASTRO REALIZADO COM SUCESSO')

                else:
                    menu.titulos('FALHA AO REALIZAR CADASTRO')
                    menu.titulos('O email ja existe na base de dados')
                    sleep(1)

            # Logica para realizar login
            elif opcao == 2:
                menu.titulos('AREA DE LOGIN')
                email = input('Digite o email: ')
                senha = input('Digite a senha: ')
                logado = True

                # Funcao para fazer authentificaçao
                # Se True = Login com sucesso
                # Se False volta ao menu principal acusando erro de email ou
                # senha
                if arquivos_registro.realiza_login(
                    usuarios, email, senha
                ):
                    menu.titulos('LOGIN REALIZADO COM SUCESSO')
                    sleep(0.5)
                    os.system('cls')

                    # Loop interno, para realizacao de leitura, atualizacao
                    # e delete para concluir o CRUD
                    while logado:
                        menu.titulos('DADOS DO USUARIO')
                        # Leitura (READ)
                        # Le apenas o usuario logado em questao
                        arquivos_registro.mostrar_dados_usuario(
                            usuarios, email
                        )
                        menu.linhas()
                        menu.menu(MENU_LOGIN)
                        opcao = menu.ler_inteiro('Escolha uma opçao>> ')
                        os.system('cls')

                        if opcao == 1:
                            # Atualicaçao (UPDATE)
                            menu.titulos('Atualizando dados')
                            arquivos_registro.mostrar_dados_para_atualizar(
                                usuarios, email
                            )

                        elif opcao == 2:
                            ...

                        elif opcao == 3:
                            menu.titulos('Retornando ao MENU PRINCIPAL...')
                            sleep(1)
                            menu.titulos('ATE BREVE!!')
                            os.system('cls')
                            logado = False

                        elif opcao not in range(1, 3):
                            menu.titulos(
                                'Erro! Opçao invalida, tente novamente'
                            )

                else:
                    menu.titulos('Erro!!! Email ou senha invalido')

            # Logica para finalizar sistema
            elif opcao == 3:
                menu.titulos('Finalizando...')
                sleep(1)  # Funcao para delay de 1 segundo
                sistema_principal = False

            # Verificando se a opcao esta entre as opcoes validas
            elif opcao not in range(1, 3):
                print('Erro!!! Opçao invalida, tente novamente')

        # Tratanto um "keyboardinterrupt"
        except KeyboardInterrupt as error:
            print(f'Error: ({type(error).__name__})')
            menu.titulos('Finalizando...')
            sleep(1)  # Funcao para delay de 1 segundo
            sistema_principal = False

# Limpa o terminal utilizando "os"
os.system('cls')
menu.titulos('VOLTE SEMPRE!!!')

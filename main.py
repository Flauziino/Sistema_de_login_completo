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

            # Logica para realizar cadastro
            if opcao == 1:
                menu.titulos('AREA DE CADASTRO')

                nome = str(input('Digite o seu primeiro nome: ')).strip()
                ultimo_nome = str(
                    input('Digite o seu ultimo nome: ')
                )
                email = input('Digite um email: ')
                senha_1 = input('Digite uma senha: ')
                senha_2 = input('Confirme a senha: ')

                user = diretorio_usuario.with_credentials(
                    nome,
                    ultimo_nome,
                    email,
                    senha_1,
                    senha_2
                )

                user_dict = dict(
                    primeiro_nome=user.primeiro_nome,
                    ultimo_nome=user.ultimo_nome,
                    email=user.email,
                    senha=user.senha
                )

                arquivos_registro.salva_usuario(usuarios, user_dict)

            # Logica para realizar login
            elif opcao == 2:
                menu.titulos('AREA DE LOGIN')
                email = input('Digite o email: ')
                senha = input('Digite a senha: ')
                arquivos_registro.realiza_login(usuarios, email, senha)

            # Logica para finalizar sistema
            elif opcao == 3:
                menu.titulos('Finalizando...')
                sleep(1)
                sistema_principal = False

            # Verificando se a opcao esta entre as opcoes validas
            elif opcao not in range(1, 3):
                print('Erro!!! Opçao invalida, tente novamente')

        # Tratanto um "keyboardinterrupt"
        except KeyboardInterrupt as error:
            print(f'Error: ({type(error).__name__})')
            menu.titulos('Finalizando...')
            sleep(1)
            sistema_principal = False

os.system('cls')
menu.titulos('VOLTE SEMPRE!!!')

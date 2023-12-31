import json
from dados_menu import menu


# Funcao para verificar se o arquivo existe
# Retorna False se nao for encontrado
# True para encontrado.
def verifica_arquivo(arquivo):
    try:
        a = open(arquivo, 'r')
        a.close()

    except FileNotFoundError as e:
        print(
            f'O arquivo ({arquivo}) nao foi encontrado! '
            f'Error>> ({type(e).__name__})'
        )
        return False

    else:
        return True


# Funcao para criar o arquivo caso a funcao anterior retorne False
def cria_arquivo(arquivo):
    try:
        a = open(arquivo, 'w')
        a.close()

    except (FileNotFoundError) as error:
        print(
            f'O arquivo ({arquivo}) nao foi encontrado! '
            f'Erro>> ({type(error).__name__})'
        )

    else:
        print(f'Arquivo ({arquivo}) criado com sucesso!')


# Funcao para escrever/salvar o usuario em json
def salva_usuario(arquivo, dict):
    try:
        # Tenta abrir o arquivo existente
        with open(arquivo, 'r') as arq:
            lista_credenciais = json.load(arq)

    # Tratando erro em caso o arquivo nao ser encontrado
    except FileNotFoundError as error:
        print(
            f'O arquivo ({arquivo}) nao foi encontrado! '
            f'Erro>> ({type(error).__name__})'
        )
        # Se o arquivo não existir ou estiver vazio, inicia uma lista vazia
        lista_credenciais = []

    # Tratando erro de decodificaçao do arquivo jSON
    except json.decoder.JSONDecodeError as error:
        print(
            f'Erro ao decodificar o arquivo ({arquivo})! '
            f'Erro>> ({type(error).__name__})'
        )
        # Se o arquivo não existir ou estiver vazio, inicia uma lista vazia
        lista_credenciais = []

    # Adiciona o novo usuário à lista de usuários
    lista_credenciais.append(dict)

    try:
        # Tenta abrir o arquivo para adicionar a lista contendo os dados
        # do usuario dentro do json
        with open(arquivo, 'w') as arq:
            json.dump(lista_credenciais, arq, ensure_ascii=False, indent=2)

    # Trata o erro caso arquivo nao seja encontrado
    except (FileNotFoundError) as error:
        print(
            f'Arquivo ({arquivo}) nao encontrado! '
            f'Error>> ({type(error).__name__})'
        )


# Funçao para realizar o login do usuario
def realiza_login(arquivo, email, senha):
    try:
        # Tenta abrir o arquivo para ler os dados
        with open(arquivo, 'r') as arq:
            lista_usuarios = json.load(arq)

            # primeiro loop para ler os arquivos do json.load (uma lista)
            for usuario in lista_usuarios:

                # verifica se o email pertence a algum usuario
                if usuario['email'] == email:
                    # verifica se a senha esta correta
                    if usuario['senha'] == senha:
                        print('LOGIN REALIZADO COM SUCESSO')
                        # retornando True para poder realizar a logica
                        # de autenticaçao
                        return True

            print('ERRO!')
            print('Email ou senha incorretos')
            return False

    except FileNotFoundError as error:
        print(f'Erro>> ({type(error).__name__})')


# Ler usuario para validar cadastro
# caso o email ja conste no sistema recusa.
def validacao_cadastro(arquivo, email):
    try:
        # Tenta abrir o arquivo para leitura do json
        with open(arquivo, 'r') as arq:
            lista_cadastros = json.load(arq)

            email_existe = False  # Variavel para rastrear o email

            # Loop para verificar os dados dentro do json
            for usuarios in lista_cadastros:
                if email == usuarios['email']:
                    email_existe = True
                    break  # Se email for encontrado nao tem pq continuar...

            if email_existe:
                # Retorno para logica do cadastro
                # False (Email ja existe)
                return False

            else:
                # Retorno para logica do cadastro
                # True (Email pode ser usado)
                return True

    # Tratando o erro "FileNotFound"
    except FileNotFoundError as error:
        print(f'Erro>> ({type(error).__name__})')


# Funcao para mostrar dados do usuario apos login
def mostrar_dados_usuario(arquivo, email):
    try:
        with open(arquivo, 'r') as arq:
            # Pegando todos os arquivos salvos na "base de dados"(jSON)
            usuarios = json.load(arq)

            # Loop na lista
            for usuario in usuarios:
                # Loop dos dicts dentro da lista
                for k, v in usuario.items():
                    # Logica para mostrar dados apenas do usuario logado
                    if email == usuario['email']:
                        print(f'   {k.upper().ljust(30)} {v}')

    # Tratando o erro "FileNotFound"
    except FileNotFoundError as error:
        print(f'Erro>> ({type(error).__name__})')

    # Tratando erro de leitura do json
    except json.JSONDecodeError as error_2:
        print(f'Erro>> ({type(error_2).__name__})')


# Funcao para mostrar dados do usuario para atualizacao (UPDATE)
# Funcao longa apenas para que ela seja unicamente para a funcionalidade de
# atualizar os dados
def mostrar_dados_para_atualizar(arquivo, email):
    try:
        with open(arquivo, 'r') as arq:
            # pegando todos os arquivos(usuarios) da base de dados (jSON)
            usuarios = json.load(arq)

            for usuario in usuarios:
                # Logica para mostrar ao usuario apenas seus proprios dados
                if email == usuario['email']:
                    print('Opçoes disponiveis para atualizar:')

                    # Loop mostrando as chaves enumeradas para realizar
                    # uma seleçao mais automatica, sem hardcoded
                    for key, value in enumerate(usuario.keys()):
                        print(f'{key} - {value}')

                    # Converte choice para um inteiro
                    choice = int(input(
                        'O que vc deseja atualizar? '
                        )
                    )

                    # Verifica se a escolha esta entre o range de opçoes
                    if choice >= 0 and choice <= len(usuario):
                        # Obtendo a chave correspondente ao indice
                        keys = list(usuario.keys())
                        chave_escolhida = keys[choice]

                        # Logica para troca de senha
                        # Atualizar a senha apenas quando ela for digitada
                        # igualmente 2 vezes
                        if chave_escolhida == 'senha':
                            senha1 = input('Digite a senha: ')
                            senha2 = input('Confirme a senha: ')
                            if senha1 == senha2:
                                usuario[chave_escolhida] = senha1

                        # Checando se o novo email nao existe na base de dados
                        elif chave_escolhida == 'email':
                            # Novo email
                            novo_email = input('Digite novo email: ')

                            email_existe = False
                            # Verificando se o email existe em algum outro
                            # Usuario
                            for user in usuarios:
                                if novo_email == user['email'] \
                                  and novo_email != email:
                                    email_existe = True
                                    break  # Caso email seja encontrado

                            if email_existe:
                                menu.titulos(
                                    'Erro ao atualizar email: JA EXISTE'
                                )

                            else:
                                usuario[chave_escolhida] = novo_email
                                menu.titulos(
                                    'Email atualizado com sucesso'
                                )

                        else:
                            novo_valor = input(
                                f'Digite o novo valor para {chave_escolhida}: '
                            )
                            usuario[chave_escolhida] = novo_valor
                            menu.titulos(
                                f'{chave_escolhida} atualizada com sucesso!'
                            )
                    else:
                        print('Opçao invalida')

        # Atualiza os dados do usuario apos editar
        with open(arquivo, 'w') as arq:
            json.dump(usuarios, arq, ensure_ascii=False, indent=2)

    # Tratando o erro "FileNotFound"
    except FileNotFoundError as error:
        print(f'Erro>> ({type(error).__name__})')

    # Tratando erro de leitura do json
    except json.JSONDecodeError as error_2:
        print(f'Erro>> ({type(error_2).__name__})')


# Funcao para deletar os dados do usuario (DELETE)
def mostrar_dados_para_deletar(arquivo, email):
    try:
        # Abre o arquivo em leitura
        with open(arquivo, 'r') as arq:
            # extrai a lista de todos usuarios
            lista_usuarios = json.load(arq)

            # loop para entrar nos dicts dentro da lista
            for usuario in lista_usuarios:
                # checagem para mostrar apenas os dados de quem esta logado
                if email == usuario['email']:
                    # confirmacao para saber se o usuario tem certeza que
                    # deseja deletar sua conta
                    check = input(
                        'Tem certeza que deseja apagar a conta? [S/N] '
                    ).strip().upper()[0]

                    if check in 'Ss':
                        lista_usuarios.remove(usuario)
                        menu.titulos('Usuario apagado com sucesso!')

        # adiciona no jSON os novos dados, apos o usuario ter deletado sua
        # conta
        with open(arquivo, 'w') as arq:
            json.dump(lista_usuarios, arq, ensure_ascii=False, indent=2)

    # Tratando o erro "FileNotFound"
    except FileNotFoundError as error:
        print(f'Erro>> ({type(error).__name__})')

    # Tratando erro de leitura do json
    except json.JSONDecodeError as error_2:
        print(f'Erro>> ({type(error_2).__name__})')


if __name__ == '__main__':
    email = 'edu@email'
    arquivo = 'usuarios.json'
    print()
    # validacao_cadastro('usuarios.json', email)
    mostrar_dados_usuario(arquivo, email)
    # mostrar_dados_para_atualizar(arquivo, email)
    mostrar_dados_para_deletar(arquivo, email)

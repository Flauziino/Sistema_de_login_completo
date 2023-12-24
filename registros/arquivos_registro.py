import json


# Funcao para verificar se o arquivo existe
# Retorna False se nao for encontrado
# True para encontrado.
def verifica_arquivo(arquivo):
    try:
        a = open(arquivo, 'r')
        a.close()

    except FileNotFoundError as e:
        print(f'O arquivo ({arquivo}) nao foi encontrado! >> ({e})')
        return False

    else:
        return True


# Funcao para criar o arquivo caso a funcao anterior retorne False
def cria_arquivo(arquivo):
    try:
        a = open(arquivo, 'w')
        a.close()

    except (FileNotFoundError) as error:
        print(f'O arquivo ({arquivo}) nao foi encontrado!\nErro>> ({error})')

    else:
        print(f'({arquivo}) criado com sucesso!')


# Funcao para escrever/salvar o usuario em json
def salva_usuario(arquivo, firstname, lastname, email, senha):
    # Cria um dicionário para o novo usuário
    usuario = {
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'senha': senha
    }

    try:
        # Tenta abrir o arquivo existente
        with open(arquivo, 'r') as arq:
            lista_credenciais = json.load(arq)

    # Tratando erro em caso o arquivo nao ser encontrado
    except FileNotFoundError as error:
        print(f'O arquivo ({arquivo}) nao foi encontrado!\nErro>> ({error})')
        # Se o arquivo não existir ou estiver vazio, inicia uma lista vazia
        lista_credenciais = []

    # Tratando erro de decodificaçao do arquivo jSON
    except json.decoder.JSONDecodeError as error:
        print(f'Erro ao decodificar o arquivo ({arquivo})!\nErro>> ({error})')
        # Se o arquivo não existir ou estiver vazio, inicia uma lista vazia
        lista_credenciais = []

    # Adiciona o novo usuário à lista de usuários
    lista_credenciais.append(usuario)

    try:
        # Tenta abrir o arquivo para adicionar a lista contendo os dados
        # do usuario dentro do json
        with open(arquivo, 'w') as arq:
            json.dump(lista_credenciais, arq, ensure_ascii=False, indent=2)

    # Trata o erro caso arquivo nao seja encontrado
    except (FileNotFoundError) as error:
        print(f'Arquivo ({arquivo}) nao encontrado!\n ({error})')

    else:
        # Confirma que tudo correu bem com o cadastro
        print('USUARIO FOI REGISTRADO COM SUCESSO!!!')


# Funçao para realizar o login do usuario
def realiza_login(arquivo, email, senha):
    try:
        # Tenta abrir o arquivo para ler os dados
        with open(arquivo, 'r') as arq:
            lista_usuarios = json.load(arq)

            # primeiro loot para ler os arquivos do json.load (uma lista)
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
        print(f'Erro>> ({error})')

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
        print(f'O arquivo ({arquivo}) nao foi encontrado! >> ({error})')

    else:
        print(f'({arquivo}) criado com sucesso!')

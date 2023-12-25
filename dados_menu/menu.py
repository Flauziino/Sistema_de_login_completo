# Funçao para linhas de separaçao
def linhas(tam=60):
    print('-'*tam)


# Funcao para titulos
def titulos(txt):
    linhas()
    print(f'{txt.center(60)}')
    linhas()


# Funcao para o menu em si
def menu(lista):
    for i in lista:
        print(f'       {i}')
    linhas()


# Funcao para validar se a entrada é de um numero inteiro valido
def ler_inteiro(txt):
    while True:
        try:
            n = input(txt)
            if n.isdigit():
                num = int(n)
                return num

        except ValueError:
            raise ValueError

        except KeyboardInterrupt:
            print('Parada forçada')
            raise KeyboardInterrupt

        else:
            print()
            print('Erro! Digite um numero inteiro!')
            print()


if __name__ == '__main__':
    opc = [
        '1. ola',
        '2. hero'
    ]
    titulos('MAIN MENU')
    menu(opc)
    ler_inteiro('Digite um numero: ')

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '..'
            )
        )
    )
except ImportError:
    raise ImportError


import os
import json
import unittest
from registros import arquivos_registro


class TesteArquivosRegistro(unittest.TestCase):

    def setUp(self):
        # Variaveis para usos futuros
        self.teste = 'teste.json'
        self.existing_data = [
            {
                'primeiro_nome': 'Maria',
                'ultimo_nome': 'Santos',
                'email': 'maria@example.com',
                'senha': '456'
            }
        ]
        self.test_dict = {
            'primeiro_nome': 'Pedro',
            'ultimo_nome': 'Souza',
            'email': 'pedro@example.com',
            'senha': '789'
        }

        # Cria um arquivo para testes
        try:
            arquivo = open(self.teste, 'w')
            arquivo.close()

        except (FileNotFoundError) as error:
            print(
                f'O arquivo ({self}) nao foi encontrado! '
                f'Erro>> ({type(error).__name__})'
            )

        else:
            print(f'Arquivo ({self}) criado com sucesso!')

    def tearDown(self):
        # Deleta os asquivos criados para teste
        os.remove(self.teste)

    def test_verifica_arquivo(self):
        # Teste para verificar se o arquivo existe
        resultado = arquivos_registro.verifica_arquivo(self.teste)
        self.assertTrue(resultado)

    def test_verifica_arquivo_nao_existe(self):
        # Teste para verificar se o arquivo NAO existe
        resultado = arquivos_registro.verifica_arquivo('arquivinho.json')
        self.assertFalse(resultado)

    def test_cria_arquivo(self):
        # Teste para criar um arquivo
        arquivos_registro.cria_arquivo('arquivo_novo.json')
        resultado = arquivos_registro.verifica_arquivo('arquivo_novo.json')
        self.assertTrue(resultado)

    def test_salva_usuario(self):
        # Teste para salvar um usuario em json
        with open(self.teste, 'w') as f:
            # escrevendo o dado existente
            json.dump(self.existing_data, f)

        # adicionando o novo dict no arquivo
        arquivos_registro.salva_usuario(self.teste, self.test_dict)

        with open(self.teste, 'r') as f:
            data = json.load(f)
            # verificando se o arquivo tem 2 conjuntos de dados (2 dicts)
            self.assertEqual(len(data), 2)
            self.assertIn(self.test_dict, data)

    def test_realiza_login_sucesso(self):
        # testando credenciais corretas
        with open(self.teste, 'w') as f:
            # escrevendo o dado existente
            json.dump(self.existing_data, f)

        # Verifica se esta tudo correto, True = True
        self.assertTrue(
            arquivos_registro.realiza_login(
                self.teste, 'maria@example.com', '456'
            )
        )

    def test_realiza_login_email_incorreto(self):
        # testando credenciais corretas
        with open(self.teste, 'w') as f:
            # escrevendo o dado existente
            json.dump(self.existing_data, f)

        # Verifica se o email nao existe, tem que retornar False = False
        self.assertFalse(
            arquivos_registro.realiza_login(
                self.teste, 'maria2@example.com', '456'
            )
        )

    def test_realiza_login_senha_incorreta(self):
        # testando credenciais corretas
        with open(self.teste, 'w') as f:
            # escrevendo o dado existente
            json.dump(self.existing_data, f)

        # Verifica se a senha esta incorreta, tem que retornar False = False
        self.assertFalse(
            arquivos_registro.realiza_login(
                self.teste, 'maria@example.com', '4599'
            )
        )


if __name__ == '__main__':
    unittest.main()

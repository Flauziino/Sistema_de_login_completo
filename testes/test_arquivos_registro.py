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
from unittest.mock import patch


class TesteArquivosRegistro(unittest.TestCase):

    def setUp(self):
        # Variaveis para usos futuros
        self.arquivo = 'usuarios.json'
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

    def test_validacao_cadastro_email_ja_existe(self):
        # testando o cadastro caso o email ja exista
        with open(self.teste, 'w') as f:
            # escrevendo o dado existente
            json.dump(self.existing_data, f)

        # verifica se o email ja existe no sistema
        # a funcao retorna False nesse caso, espera-se False = False
        self.assertFalse(
            arquivos_registro.validacao_cadastro(
                self.teste, 'maria@example.com'
            )
        )

    def test_validacao_cadastro_email_nao_existe(self):
        # testando o cadastro caso o email nao exista
        with open(self.teste, 'w') as f:
            # escrevendo o dado existente
            json.dump(self.existing_data, f)

        # verifica se o email nao existe no sistema
        # a funcao retorna True nesse caso, espera-se True = True
        self.assertTrue(
            arquivos_registro.validacao_cadastro(
                self.teste, 'edu@example.com'
            )
        )

    # Teste para troca da senha (func mostrar_dados_para_atualizar)
    # simulando input do usuario de 3 (para senha)
    # e mudando ela para 'nova_senha'
    @patch('builtins.input', side_effect=['3', 'nova_senha', 'nova_senha'])
    def test_mostrar_dados_para_atualizar_senha(self, mock_input):
        with open(self.teste, 'w') as f:
            # escrevendo o dado existente
            json.dump(self.existing_data, f)

        # Obtendo a senha antes da atualização
        with open(self.teste, 'r') as arq:
            usuarios = json.load(arq)
        resultado_esperado = usuarios[0]['senha']

        # Chamando a função a ser testada
        arquivos_registro.mostrar_dados_para_atualizar(
            self.teste, 'maria@example.com'
            )

        # Obtendo a senha após a atualização
        with open(self.teste, 'r') as arq:
            usuarios_atualizados = json.load(arq)
        resultado_obtido = usuarios_atualizados[0]['senha']

        # Verificando se a senha foi alterada corretamente
        self.assertNotEqual(resultado_esperado, resultado_obtido)

    # Teste para troca do primeiro_nome (func mostrar_dados_para_atualizar)
    # simulando input do usuario de 0 (para primeiro_nome)
    # e mudando ele para felix
    @patch('builtins.input', side_effect=['0', 'felix'])
    def test_mostrar_dados_para_atualizar_primeiro_nome(self, mock_input):
        with open(self.teste, 'w') as f:
            # escrevendo o dado existente
            json.dump(self.existing_data, f)

        # Obtendo o primeiro_nome antes da atualização
        with open(self.teste, 'r') as arq:
            usuarios = json.load(arq)
        resultado_esperado = usuarios[0]['primeiro_nome']

        # Chamando a função a ser testada
        arquivos_registro.mostrar_dados_para_atualizar(
            self.teste, 'maria@example.com'
            )

        # Obtendo o primeiro_nome após a atualização
        with open(self.teste, 'r') as arq:
            usuarios_atualizados = json.load(arq)
        resultado_obtido = usuarios_atualizados[0]['primeiro_nome']

        # Verificando se o primeiro_nome foi alterada corretamente
        self.assertNotEqual(resultado_esperado, resultado_obtido)

    # Teste para troca do ultimo_nome (func mostrar_dados_para_atualizar)
    # simulando input do usuario de 1 (para ultimo_nome)
    # e mudando ele para pereira
    @patch('builtins.input', side_effect=['1', 'pereira'])
    def test_mostrar_dados_para_atualizar_ultimo_nome(self, mock_input):
        with open(self.teste, 'w') as f:
            # escrevendo o dado existente
            json.dump(self.existing_data, f)

        # Obtendo o ultimo_nome antes da atualização
        with open(self.teste, 'r') as arq:
            usuarios = json.load(arq)
        resultado_esperado = usuarios[0]['ultimo_nome']

        # Chamando a função a ser testada
        arquivos_registro.mostrar_dados_para_atualizar(
            self.teste, 'maria@example.com'
            )

        # Obtendo o ultimo_nome após a atualização
        with open(self.teste, 'r') as arq:
            usuarios_atualizados = json.load(arq)
        resultado_obtido = usuarios_atualizados[0]['ultimo_nome']

        # Verificando se o ultimo_nome foi alterada corretamente
        self.assertNotEqual(resultado_esperado, resultado_obtido)

    # Teste para troca de email (func mostrar_dados_para_atualizar)
    # simulando input do usuario de 2 (para email) e mudando email para
    # mari@email
    @patch('builtins.input', side_effect=['2', 'mari@email'])
    def test_mostrar_dados_para_atualizar_email(self, mock_input):
        with open(self.teste, 'w') as f:
            # escrevendo o dado existente
            json.dump(self.existing_data, f)

        # Obtendo o email antes da atualização
        with open(self.teste, 'r') as arq:
            usuarios = json.load(arq)
        resultado_esperado = usuarios[0]['email']

        # Chamando a função a ser testada
        arquivos_registro.mostrar_dados_para_atualizar(
            self.teste, 'maria@example.com'
            )

        # Obtendo o email após a atualização
        with open(self.teste, 'r') as arq:
            usuarios_atualizados = json.load(arq)
        resultado_obtido = usuarios_atualizados[0]['email']

        # Verificando se o email foi alterada corretamente
        self.assertNotEqual(resultado_esperado, resultado_obtido)

    # Teste para funcao mostrar dados_para_deletar
    @patch('builtins.input', side_effect=['S'])
    def test_deletar_conta(self, mock_input):
        with open(self.teste, 'w') as f:
            # escrevendo o dado existente
            json.dump(self.existing_data, f)

        # adicionando o novo dict no arquivo
        arquivos_registro.salva_usuario(self.teste, self.test_dict)

        # Chama a função que deleta a conta
        arquivos_registro.mostrar_dados_para_deletar(
            self.arquivo, 'pedro@example.com'
            )

        # Verifica se o usuário foi removido da lista
        with open(self.arquivo, 'r') as arq:
            usuarios_atualizados = json.load(arq)

        # Verifica se o usuário foi removido
        usuario_deletado = next(
            (
                user for user in usuarios_atualizados
                if user['email'] == 'pedro@example.com'
            ), None
        )
        self.assertIsNone(usuario_deletado)


if __name__ == '__main__':
    unittest.main()

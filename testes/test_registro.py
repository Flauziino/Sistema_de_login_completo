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

import unittest
from registros import registro


class TestUsuarioClasses(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        self.user_builder = registro.UsuarioConstrutor()
        self.diretorio_usuario = registro.DiretorioUsuario(self.user_builder)

    def test_usuario_creation(self):
        # Testa se a criação de um usuário inicializa corretamente seus campos
        user = registro.Usuario()
        self.assertIsNotNone(user)
        self.assertIsNone(user.primeiro_nome)
        self.assertIsNone(user.ultimo_nome)
        self.assertIsNone(user.email)
        self.assertIsNone(user.senha)

    def test_usuario_construtor_reset(self):
        # Testa se o método reset do construtor de usuário reinicia corretamente os campos
        user = self.user_builder.result
        user.primeiro_nome = "Alice"
        user.ultimo_nome = "Smith"
        user.email = "alice@example.com"
        user.senha = "12345"

        self.user_builder.reset()
        reset_user = self.user_builder.result

        self.assertIsNotNone(reset_user)
        self.assertIsNone(reset_user.primeiro_nome)
        self.assertIsNone(reset_user.ultimo_nome)
        self.assertIsNone(reset_user.email)
        self.assertIsNone(reset_user.senha)

    def test_diretorio_usuario_with_matching_passwords(self):
        # Testa se o diretório de usuário cria um usuário corretamente quando as senhas coincidem
        user = self.diretorio_usuario.with_credentials("Alice", "Smith", "alice@example.com", "password", "password")
        self.assertIsNotNone(user)
        self.assertEqual(user.primeiro_nome, "Alice")
        self.assertEqual(user.ultimo_nome, "Smith")
        self.assertEqual(user.email, "alice@example.com")
        self.assertEqual(user.senha, "password")

    def test_diretorio_usuario_with_mismatching_passwords(self):
        # Testa se o diretório de usuário não cria um usuário quando as senhas não coincidem
        user = self.diretorio_usuario.with_credentials("Bob", "Johnson", "bob@example.com", "senha", "password")
        self.assertIsNone(user)


if __name__ == '__main__':
    unittest.main()

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
from unittest import mock
from dados_menu import menu


class TestMenu(unittest.TestCase):

    def test_lerint(self):
        # Teste para entrada correta de numero inteiro
        # Simula a entrada do usuario como '5' e verifica se o retorno é 5
        with mock.patch('builtins.input', return_value='5'):
            resultado = menu.ler_inteiro('Digite um numero: ')
            self.assertEqual(resultado, 5)

        # Teste para entrada recebendo strings do usuario
        # Simula a entrada do usuario como 'abc' e verifica se retorna um erro
        with mock.patch('builtins.input', side_effect=[
            'abc', 'dedaw', ' ', '7'
            ]
        ):
            resultado = menu.ler_inteiro('Digite um numero: ')
            self.assertEqual(resultado, 7)


if __name__ == '__main__':
    unittest.main()

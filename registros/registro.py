from abc import ABC, abstractmethod


# Classe para registrar o usuario
# Utilizando padrao de projeto "Builder"
# Usado apenas para praticar classes e padrao de projeto
class Usuario:
    def __init__(self):
        self.primeiro_nome = None
        self.ultimo_nome = None
        self.email = None
        self.senha = None

    def __str__(self):
        attr = ', '.join(
            [f'{k} = {v}' for k, v in self.__dict__.items()]
        )
        class_name = type(self).__name__
        return f'{class_name}: ({attr})'

    def __repr__(self):
        return self.__str__()


class IUsuarioConstrutor(ABC):
    @property
    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def get_firstname(self):
        pass

    @abstractmethod
    def get_lastname(self):
        pass

    @abstractmethod
    def get_email(self):
        pass


class UsuarioConstrutor(IUsuarioConstrutor):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = Usuario()

    @property
    def result(self):
        retorno_dados = self._result
        self.reset()
        return retorno_dados

    def get_firstname(self, firstname):
        self._result.primeiro_nome = firstname
        return self

    def get_lastname(self, lastname):
        self._result.ultimo_nome = lastname
        return self

    def get_email(self, email):
        self._result.email = email
        return self

    def get_senha(self, senha):
        self._result.senha = senha
        return self


class DiretorioUsuario:
    def __init__(self, construtor: UsuarioConstrutor):
        self._construtor = construtor

    def with_email(self, firstname, lastname, email):

        self._construtor.get_firstname(firstname)\
            .get_lastname(lastname)\
            .get_email(email)

        return self._construtor.result

    def with_senha(self, firstname, senha_1, senha_2):
        self._construtor.get_firstname(firstname)

        if senha_1 == senha_2:
            self._construtor.get_senha
            return self._construtor.result
        print('Senha 1 tem que ser igual senha 2')


if __name__ == '__main__':
    user_builder = UsuarioConstrutor()
    diretorio_usuario = DiretorioUsuario(user_builder)

    user1 = diretorio_usuario.with_email(
        'Joao', 'Carlos', 'carlos@email.com'
    )
    print(user1)

    user1 = diretorio_usuario.with_senha('Joao', 123, 123)
    print(user1)

# coding: utf-8

class DataTable:
    """
    Representa uma tabela de dados

    Essa classe representa uma tabela de dados do Portal da transparência do Governo Federal.
    Deve ser capaz de validar linhas inseridas de acordo com o layout estabelecido

    Attributes:
        name: Nome da tabela
        columns: [Lista de Colunas]
        data: [Lista de dados]

    """

    def __init__(self, name):
        """
        Construtor da classe DataTable

        :param nome: Nome da tabela
        """
        self._name = name
        self._columns = []
        self._data = []

    @property
    def name(self):
        return self._name

    @property
    def columns(self):
        return self._columns

    @property
    def data(self):
        return self._data


class Column:
    """
    Classe que representa a coluna de uma Tabela no banco de dados
    """

    def __init__(self, name, kind, description):
        """
        Construtor da classe que representa a coluna de uma Tabela no banco de dados

        :param nome: xxxx
        :param kind: xxxx
        :param description: xxxx
        """

        self._name = name
        self._kind = kind
        self._description = description


if __name__ == '__main__':
    print(Column.__init__.__doc__)

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
        self._references = []
        self._referenced = []

    @property
    def name(self):
        return self._name

    @property
    def columns(self):
        return self._columns

    @property
    def data(self):
        return self._data

    def add_column(self, name, kind, desciption=""):
        column = Column(name, kind, desciption)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        """
        Cria uma referencia dessa Tabela para uma Tabela

        :param name: Nome da relação
        :params to: instancia da tabela apontada
        :params on: instancia coluna em que existe a relação (troca de chaves - PK, FK)
        :return:
        """
        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        """
        Cria uma referencia dessa Tabela para uma Tabela

        :param name: Nome da relação
        :params by: instancia da tabela apontada
        :params on: instancia coluna em que existe a relação (troca de chaves - PK, FK)
        :return:
        """
        relationship = Relationship(name, self, by, on)
        self._referenced.append(relationship)


class Column:
    """
    Classe que representa a coluna de uma Tabela no banco de dados
    """

    def __init__(self, name, kind, description=None):
        """
        Construtor da classe que representa a coluna de uma Tabela no banco de dados

        :param nome: xxxx
        :param kind: xxxx
        :param description: xxxx
        """

        self._name = name
        self._kind = kind
        self._description = description
        self._is_pk = False

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name, self._kind, self._description)
        return _str


class Relationship:
    """
    Classe que representa uma relacionamento entre DataTables
    """

    def __init__(self, name, _from, to, on):
        self._name = name
        self._from = _from
        self._to = to
        self._on = on


class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=None):
        super().__init__(name, kind, description=description)
        self._is_pk = True

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name, self._kind, self._description)
        return "{} - {}".format("PK", _str)


if __name__ == '__main__':
    table_empreendimento = DataTable("Empreendimento")
    col_id = table_empreendimento.add_column("IdEmpreendimento", "bigint")
    col_aditivo = table_empreendimento.add_column("IdAditivo", "bigint")
    col_alerta = table_empreendimento.add_column("IdAlerta", "bigint")

    table_aditivo = DataTable("Aditivo")
    col_id = table_empreendimento.add_column("IdAditivo", "bigint")
    col_emp_id = table_empreendimento.add_column("IdEmpreendimento", "bigint")

    table_empreendimento.add_references("IdAdivito", table_aditivo, col_aditivo)
    table_empreendimento.add_references("IdEmpreendimento", table_empreendimento, col_emp_id)

    print(table_empreendimento)
    print(table_aditivo)

    table = DataTable("Empreendimento")
    print(Column("IdEmpreendimento", "bigint"))
    print(PrimaryKey(table, "IdEmpreendimento", "bigint"))

    table = DataTable("Empreendimento")
    print(Column("IdEmpreendimento", "bigint"))
    print(PrimaryKey(table, "IdEmpreendimento", "bigint"))

# coding: utf-8

"""
Classe que representa o aluno com as suas 3 notas
"""


class Aluno():
    """
        Representa um aluno

        Attributes:
            nota1: Primeira nota
            nota2: Segunda nota
            nota3: Terceira nota

    """

    def __init__(self, nota1, nota2, nota3):
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota3 = nota3

    @property
    def nota1(self):
        return self._nota1

    @property
    def nota2(self):
        return self._nota2

    @property
    def nota3(self):
        return self._nota3

    def calcula_media(self):
        """
            Método calcula_media

            Ele calcula as média das 3 notas que o aluno possui e imprime um boletim
            com as notas arredondadas e a média com somente duas casas decimais
        """
        media = round(((self.nota1 + self.nota2 + self.nota3) / 3), 2)

        print("\n------------- Boletim -------------")
        print("\nNota 1: {}".format(self.nota1))
        print("Nota 2: {}".format(self.nota2))
        print("Nota 3: {}".format(self.nota3))

        print("\nA média do aluno é: {}".format(media))
        print("---------------------------------")


def inputNota(texto):
    """
    Método inputNota

    Esse método serve para pegar a nota que o usuário digitar e tratar possiveis erros
    caso tenha algum erro, por exemplo digitar texto no campo de número

    E faz um loop para perguntar a nota enquanto o usuário não digita uma nota válida
    """
    nota_formato = True
    nota = None

    while (nota_formato):
        try:
            nota = float(input("Digite a " + texto + " nota do aluno: "))
            nota = round(nota)
            nota_formato = False
        except ValueError as ve:
            print('Você deve inserir um número. Ex.: (5 ou 7.5).')

    return nota


if __name__ == '__main__':
    nota1 = inputNota("primeira")
    nota2 = inputNota("segunda")
    nota3 = inputNota("terceira")

    aluno = Aluno(nota1, nota2, nota3)
    aluno.calcula_media()

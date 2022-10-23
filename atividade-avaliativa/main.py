# coding: utf-8

"""
Classe que representa o aluno com as suas 3 notas
"""


class Aluno:
    """
        Representa um aluno

        Attributes:
            nota1: Primeira nota
            nota2: Segunda nota
            nota3: Terceira nota

    """

    def __init__(self, aluno_nota1, aluno_nota2, aluno_nota3):
        self._nota1 = aluno_nota1
        self._nota2 = aluno_nota2
        self._nota3 = aluno_nota3
        self._media = 0

    @property
    def nota1(self):
        return self._nota1

    @property
    def nota2(self):
        return self._nota2

    @property
    def nota3(self):
        return self._nota3

    @property
    def media(self):
        return self._media

    @media.setter
    def media(self, media):
        self._media = media

    def calcula_media(self):
        """
            Método calcula_media

            Ele calcula as média das 3 notas que o aluno possui
            com as notas arredondadas e a média com somente duas casas decimais
        """
        media = round(((self.nota1 + self.nota2 + self.nota3) / 3), 2)
        self.media = media

    def mostrar_boletim(self):
        """
            Método mostrar_boletim

            Ele imprime as notas do aluno, a média das notas e se o aluno foi aprovado ou não.
            O aluno é aprovodo caso a nota seja maior ou igual a 5.
        """
        print("\n------------ Boletim ------------")
        print("\n\tNota 1: {}".format(self.nota1))
        print("\tNota 2: {}".format(self.nota2))
        print("\tNota 3: {}".format(self.nota3))

        print("\n\tA média do aluno é: {}".format(self.media))

        if self.media >= 5:
            print("\n\tAluno Aprovado")
        else:
            print("\n\tAluno Reprovado")

        print("---------------------------------")


def input_nota(texto):
    """
        Método input_nota

        Esse método serve para pegar a nota que o usuário digitar e tratar possiveis erros
        caso tenha algum erro, por exemplo digitar texto no campo de número

        E faz um loop para perguntar a nota enquanto o usuário não digita uma nota válida
    """
    nota_formato = True
    nota = None

    while nota_formato:
        try:
            nota = float(input("Digite a " + texto + " nota do aluno: "))
            nota = round(nota)
            nota_formato = False
        except ValueError:
            print('Você deve inserir um número. Ex.: (5 ou 7.5).')

    return nota


if __name__ == '__main__':
    nota1 = input_nota("primeira")
    nota2 = input_nota("segunda")
    nota3 = input_nota("terceira")

    aluno = Aluno(nota1, nota2, nota3)
    aluno.calcula_media()
    aluno.mostrar_boletim()

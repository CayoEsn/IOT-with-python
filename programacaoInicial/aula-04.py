from datetime import date
import math as matematica
from math import log2 as log

import matplotlib.pyplot as plt


def salario_descontado_imposto(salario, imposto=27.):
    return salario - (salario * (imposto * 0.01))


def new_user(active=False, admin=False):
    print(active)
    print(admin)


def unpacking_experiment(*args):
    arg1 = args[0]
    args2 = args[1]
    outroArgumento = args[2:]
    print(arg1)
    print(args2)
    print(outroArgumento)


def unpacking(**kwargs):
    print(kwargs)


if __name__ == '__main__':
    # d = (2022, 3, 15)
    # date(d[0], d[1], d[2])

    # datetime.date(2022, 3, 15)

    # date(*d)
    #
    # print(salario_descontado_imposto(5000, 10))
    #
    # config = {"active": False, "admin": True}
    # new_user(**config)

    # unpacking_experiment(1, 2, 3, 4, 5, 6, 7, 8, 9)
    # unpacking(name="Teste", other="Outro")
    # print(math.sqrt(256))

    # print(matematica.sqrt(1000))
    # print(log(1024))

    x = [1, 2, 3, 4]
    y = [2, 3, 4, 3]
    plt.plot(x, y)
    plt.show()

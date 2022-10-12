# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    salario = int(input("Salário: "))
    imposto = input("Imposto em % (Ex.: 27.5) ?")

    if imposto == '':
        imposto = 27.5
    else:
        imposto = float(imposto)

    print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

    if imposto < 5.:
        print("Baixo")
    elif imposto >= 5. and imposto <= 17.:
        print("Médio")
    elif imposto > 17 and imposto < 100:
        print("Alto")
    else:
        print("Imposto é inválido")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

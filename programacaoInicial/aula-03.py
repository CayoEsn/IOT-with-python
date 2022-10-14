if __name__ == '__main__':
    # print_hi('PyCharm')
    salario = int(input("Salário: "))
    imposto = input("Imposto em % (Ex.: 27.5) ? ")

    if imposto == '':
        imposto = 27.5
    else:
        imposto = float(imposto)

    print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

    if imposto < 5.:
        print("Imposto baixo")
    elif imposto >= 5. and imposto <= 17.:
        print("Imposto médio")
    elif imposto > 17 and imposto < 100:
        print("Imposto alto")
    else:
        print("Imposto é inválido")

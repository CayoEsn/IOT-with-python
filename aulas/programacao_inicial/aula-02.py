# Tipos numéricos
print(int(1.0))
print(int(9.85))
print(float(1))
print(complex(1, 2))
print(1+3)
print(10/2)
print(2^8)
print(2**8)
print(2**10)
print(10%3)
print(10/3)
print(10//3)

# Movimentações de bits
print(4 >> 2)
print(4 << 2)

# Identificando tipos
print(type(1))
print(type(1 + 2.0))
print(type(1+2j))

st = "morumbi"
print(st[0])
print(st[1:5])
print(len(st))
print("m" in st)
print("Z" in st)

minha_str = "morumbi " + "2"
print(minha_str)

print("maracana".count("a"))

print("%d dias para a copa" % 45)
print("{} dias para a copa".format(60))
print("{dias} dias para a copa".format(dias=75))

# Calculo de imposto
imposto = 0.27
salario = 5000
print("Salário real: {}".format(salario - (salario * imposto)))
print("Imposto: {}".format((salario * imposto)))
import os


def ler_diretorio_os():
    # os.listdir("/home/cayo/Documents/SENAI-BigData/Projetos/IOT-with-python/aula_06_meu_projeto_python/meta-data")
    for meta_file in os.listdir("./meta-data"):
        print(meta_file.split(".")[0])


def extract_name(name):
    return name.split(".")[0]


def read_lines(filename):
    file = open(os.path.join("./meta-data/", filename), "rt")
    data = file.read().split("\n")
    file.close()

    return data


def read_meta_data(filename):
    meta_data = []

    for column in read_lines(filename):
        if column:
            line_data = column.split("\t")
            # meta_data.insert(0, line_data[0])
            # meta_data.insert(1, line_data[1])
            # meta_data.insert(2, line_data[2])
            meta_data.append(line_data[:-1])

    return meta_data


def main():
    meta = {}

    for meta_data_file in os.listdir("./meta-data"):
        table_name = extract_name(meta_data_file)
        meta[table_name] = read_meta_data(meta_data_file)

    for key, val in meta.items():
        print("\n- Entidade: {}".format(key))
        print("- Atributos: ")
        for col in val:
            print("\t{}: {}".format(col[1], col[0]))


if __name__ == '__main__':
    main()

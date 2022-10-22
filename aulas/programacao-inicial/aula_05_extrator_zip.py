# coding: utf-8

import os.path
import sys
import zipfile


def main(path):
    if not os.path.exists(path):
        print("O arquivo {} não existe".format(path))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall("output")
        print("Arquivos extraídos")


if __name__ == '__main__':
    main(sys.argv[1])

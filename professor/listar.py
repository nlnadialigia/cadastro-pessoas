from formatacao import titulo, line


def listar():
    titulo('PESSOAS CADASTRADAS')
    try:
        arquivo = open('pessoas.txt', 'r')
        for linha in arquivo:
            linha = linha.rstrip()
            print(linha)
    except FileNotFoundError:
        arquivo = open('pessoas.txt', 'a')
    arquivo.close()

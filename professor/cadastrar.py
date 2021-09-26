from formatacao import titulo, line

pessoas = dict()


def cadastrar():
    arquivo = open('pessoas.txt', 'a')
    titulo('NOVO CADASTRO')
    try:
        pessoas['nome'] = str(input('Nome: '))
        pessoas['idade'] = int(input('Idade: '))
        arquivo.writelines(f'{pessoas["nome"]:20} {pessoas["idade"]}\n')
        print(f'Novo registro de {pessoas["nome"]} adicionado.')
    except TypeError:
        print('Dados inválidos. Tente novamente')
    except FileNotFoundError:
        arquivo = open('pessoas.txt', 'a')
        arquivo.writelines(pessoas)
    arquivo.close()
    return pessoas


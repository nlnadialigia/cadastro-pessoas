from lib.interface import *

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # listar()
        cabecalho('Opção 1')
    elif resposta == 2:
        # cadastrar()
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print(f'\033[31mERRO! Digite uma opção válida!\033[m')

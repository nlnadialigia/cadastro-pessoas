from lib.interface import *
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # listar()
        lerArquivo(arq)
    elif resposta == 2:
        # cadastrar()
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print(f'\033[31mERRO! Digite uma opção válida!\033[m')

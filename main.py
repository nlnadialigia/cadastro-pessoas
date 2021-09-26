from cadastrar import cadastrar
from formatacao import titulo, texto, vermelho, reset, line
from listar import listar

while True:
    titulo('MENU PRINCIPAL')
    texto(1, 'Ver pessoas cadastradas')
    texto(2, 'Cadastrar nova Pessoa')
    texto(3, 'Sair do Sistema')
    print(line)
    opcao = str(input('Sua Opção: '))
    if opcao == '1':
        listar()
    elif opcao == '2':
        cadastrar()
    elif opcao == '3':
        titulo('Saindo do sistema... Até logo!')
        break
    else:
        print(f'{vermelho}Opção inválida.{reset}')

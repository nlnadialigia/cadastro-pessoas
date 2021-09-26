amarelo = '\33[33m'
azul = '\33[34m'
verde = '\33[32m'
vermelho = '\33[31m'
reset = '\33[m'
space = 40
line = '*' * space


def titulo(msg):
    print(line)
    print(f'{msg}'.center(space))
    print(line)


def texto(num, msg):
    print(f'{amarelo}{num}{reset} - {azul}{msg}{reset}')



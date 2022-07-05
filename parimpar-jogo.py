print('vamos jogar par ou impar!')
from random import randint
while True:
    jogador = int(input('Digite um número: '))
    comp = randint(0,11)
    tipo = ' '
    soma = jogador + comp
    c = 0
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar[I/P]? ')).upper()
    print(f'voce jogou {jogador} e o computador jogou {comp}, total de {soma}')
    print('Deu par'if soma %2==0 else 'Deu impar')

    if tipo == 'par':
        if soma %2==0:
            print('voce ganhou')
            c += 1
        else:
            print('voce perdeu')
            break
    else:
        if soma %3==0:
            print('voce ganhou')
            c += 1
        else:
            print('voce perdeu')
            break
print(f'O JOGO ACABOU, VOCÊ GANHOU {c} vezes')
lista = []
while True:
    n = int(input('digite um numero: '))
    if n not in lista:
        lista.append(n)
    else:
        print('valor ja existe na lista')
    resp = input('Quer continuar [S/N]? ').upper()
    while resp not in 'SN':
        resp = input('Digite apenas [S/N]. ').upper()
        if resp in 'SN':
            break
    if resp in 'N':
        break
print(f'voce digitou {lista}')
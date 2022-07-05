def maior(*num):
    cont = mai = 0
    print('Os numeros analisádos foram:')
    for valor in num:
        print(f'{valor}',end=' ')
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'\n• foram informados {cont} numeros')
    print(f'• o maior numero é {mai}')
    print('='*30)


maior(1,3,5,7)
maior(9, 8, 3, 0, 4, 2)
maior(0)
maior()
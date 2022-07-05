print('=-'*5)
print('CARRINHO')
print('=-'*5)
total = qp = menor = cont = 0
barato = ' '
while True:
    prod = input('Produto: ')
    valor = float(input('Valor: '))
    cont += 1
    if cont == 1:
        menor = valor
        barato = prod
    else:
        if valor < menor:
            menor = valor
            barato = prod

    total += valor
    if valor > 1000:
        qp += 1
    seguir = ' '
    while seguir not in 'SN':
        seguir = input('Adicionar mais coisas?[S/N]').upper()
    if seguir == 'N':
        break
print(f'total de {total}')
print(f'são {qp} produtos acima de 1000R$')
print(f'o produto mais barato foi {barato} e custou {menor}')
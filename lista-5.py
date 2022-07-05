lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = input('Quer digitar outro numero? [S/N]').upper()
    if resp not in 'SN':
        print('Resposta inválida, tente novamente.',end=' ')
    if resp in 'N':
        break

print(f'{lista}')
print(f'essa lista tem {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'os numeros na ordem decrescente ficam: {lista}')
if 5 in lista:
    print('o numero 5 foi digitado')
else:
    print('não tem numero 5 na lista')

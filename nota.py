lista = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    resp = str(input('Quer continuar? [S/N]')).upper()
    lista.append([nome, [n1, n2], media])
    while resp not in 'SN':
        resp = str(input('Resposta invalida. Quer continuar? [S/N]')).upper()
    if resp == 'N':
        break
print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>8}')
print('_'* 35)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>7.1f}')
while True:
    opc = int(input('Mostrar as notas de qual aluno? '))
    if opc == 999:
        break
    if opc <= len(lista) -1:
        print(f'notas de {lista[opc][0]} são {lista[opc][1]}')
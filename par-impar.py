lista1 = []
listapar = []
listaimpar = []
while True:
    lista1.append(int(input('Digite um numero: ')))
    resp = input('Quer digitar outro numero[S/N]? ').upper()
    while resp not in 'SN':
        resp = input('Resposta inválida, Quer digitar outro numero[S/N]?').upper()
    if resp in 'N':
        break
for i, v in enumerate(lista1):
    if v % 2 == 0:
        listapar.append(v)
    elif v % 2 == 1:
        listaimpar.append(v)
print(f'a lista geral é {lista1}')
print(f'a lista de numeros impares é {listaimpar}')
print(f'a lista de numeros pares é {listapar}')
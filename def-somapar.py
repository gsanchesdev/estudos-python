from random import randint
numeros = []
def sorteia():
    for c in range(0, 5):
       numeros.append(randint(1, 10))
    print(f'Os numeros sorteados foram {numeros}')
def somapar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma entre os números pares é {soma}')
sorteia()
somapar()



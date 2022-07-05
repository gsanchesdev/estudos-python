temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = input('Quer continuar (S/N)? ').upper()
    while resp not in 'SN':
        resp = str(input('Resposta inválida. Quer continuar [S/N]?')).upper()
    if resp in 'N':
        break

print(f'os dados foram {princ}')
print(f'foram {len(princ)} pessoas cadastradas.')
print(f'o maior peso foi de {maior}kg. Peso de ',end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]',end=' ')
print()
print(f'o menor peso foi de {menor}k    g. Peso de ',end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]',end=' ')
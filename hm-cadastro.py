ci = ch = m20 = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        ci += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [F/M]: ').upper()
        if sexo == 'M':
            ch +=1
    if sexo == 'F' and idade < 20:
        m20 += 1
    seguir = ' '
    while seguir not in 'SN':
        seguir = input('dados cadastrados, quer continuar? [S/N]').upper()
    if seguir == 'N':
        break
print(f'São {ci} maiores de 18 anos, {ch} homens cadstrados e {m20} mulheres com menos de 20 anos. ')

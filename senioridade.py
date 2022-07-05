num = int(input('Digite sua idade: '))
if num < 18:
    print('Junior')
else:
    if 18 <= num < 35:
        print('adulto')
    else:
        print('senior')


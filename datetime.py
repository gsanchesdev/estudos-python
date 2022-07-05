from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nacimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0) se nao tiver.'))
if dados['ctps'] != 0:
    dados['anoc'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario: '))
    dados['apos'] = dados['idade'] + (dados['anoc'] + 35) - datetime.now().year
for k, v in dados.items():
    print(f'{k} é {v}')
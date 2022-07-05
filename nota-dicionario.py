aluno = {}
aluno['joao'] = [5.5, 6, 7.5]
aluno['ana'] = [9.2, 7, 8]
aluno['gustavo'] = [6, 7.5, 4]
aluno['marcos'] = [4, 3.6, 2]
for k, v in aluno.items():
    media = sum(v)/len(v)
    if media >= 6:
        print(f'{k} aprovado: media {media:.1f}')
    else:
        print(f'{k} reprovado: media {media:.1f}')
jogo = {}
partida = []
jogo['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogo["nome"]} jogou? '))
for c in range(0, tot):
    partida.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogo['gol'] = partida[:]
jogo['total'] = sum(partida)
print('='*30)
for k, v in jogo.items():
    print(f'{k}: {v}')
print('='*30)

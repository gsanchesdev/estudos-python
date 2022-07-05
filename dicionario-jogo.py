jogo = {}
jogo['nome'] = str(input('Nome do jogador: '))
jogo['partida'] = int(input(f'Quantas partidas {jogo["nome"]} jogou? '))
for c in range(0, jogo["partida"]):
    jogo["gol"] = int(input(f'quantos gols na partida {c+1}? '))
    



print(jogo)
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

jogador = int(input('''
Suas opções:
[0] Pedra: 
[1] Papel: 
[2] Tesoura: 
escolha sua opção: '''))

print('-='*11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*11)

sleep(1)
print('jo')
sleep(1)
print('Ken')
sleep(2)
print('pô....')
sleep(1)

if computador == 0:# computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada invalida!')

elif computador == 1:# computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada invalida!')

elif  computador == 2:# computador jogou tesoura
    if jogador == 0:
        print('JOGADOR GANHA')
    elif jogador == 1:
        print('COMPUTADOR GANHA')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida!')

n = int(input('Digite um number: '))
print(f'O fatorial de {n}!= ',end='')
inicio = n
f = 1
while inicio > 0:
    print(f'{inicio}', end='')
    print('x' if inicio > 1 else '=', end=' ')
    f *= inicio
    inicio -= 1
    
print(f'{f}')

    
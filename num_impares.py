print('\033[1;37m<'*40,'MÚLTIPLOS DE TRÊS!','>'*40)
soma = 0
for impares in range(3, 500, 6):
    print(impares)
    soma += impares
print(f'a soma dos multiplos de três do intervalo de 1 até 500 é >>> {soma}')

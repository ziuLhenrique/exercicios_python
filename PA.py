termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
for c in range(termo1, 100, razao):
    cont +=1
    print(f' {c}', end='-->')
    if cont == 10:
        #print(c, end=' ')
        break
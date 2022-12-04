print('\033[4;32m*'*40,'NÚMEROS_PRIMOS','*'*40)


num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[4;32m', end=' ')
        cont +=1
    else:
        print('\033[4;31m', end=" ")
    print(c, end=' ')
print(f'\033[m) número {num} foi  dividido {cont} VEZES')
if cont == 2:
    print('E POR ISSO ELE É PRIMO!')
else:
    print('E POR ISSO ELE NÃO É PRIMO!')


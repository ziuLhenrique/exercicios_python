print('\033[4;32m*'*40,'NÚMEROS_PRIMOS','*'*40)

num = int(input('Digite um número: '))

if num % 2 != 0:
    print(f'O número {num} é um número primo.')

else :
    print(f'O número {num} não é um número primo.') 
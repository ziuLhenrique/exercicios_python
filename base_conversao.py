num = int(input('Digite um número inteiro: '))
opcao = int(input('''
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL
sua opção: '''))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')

elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')

elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}') 

else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE!')



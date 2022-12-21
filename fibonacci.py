#Os prints com \033[1;36m SÃO PARA DAR CORES NO CÓDIGO.


print('\033[4;36m~'*50,'FIBONACCI','~'*50)
n = int(input('Type it a number: '))

t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end=" ")
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end=' ')
    
    t1 = t2
    t2 = t3
    cont +=1
print("\033[4;35m-> FIM")

















'''
def primeiro_decorator(func):

    def primeira_func():
        print('Execução antes da função')

        func()

        print('Execução depois da função')

    return  primeira_func

@primeiro_decorator
def funcao_utilizadora():
    print('Preciso utilizar o decorator')

funcao_utilizadora()
'''
def decorator_imprimir(func):

    def imprima_parametros():
        print('CAPITAL: ')
        func()
        print('taxa: ')
        func()
        print('tempo: ')
    return imprima_parametros

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa/100) * tempo

juros_simples(1000, 5, 6)




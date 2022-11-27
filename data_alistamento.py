from datetime import date 

atual = date.today().year
nasc = int (input('Ano de nacimento: '))
sexo = int(input('''
Qual seu sexo?  
[1] Masculino
[2] Feminino
digite seu sexo: '''))
idade = atual - nasc

print (f'Quen nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18 and sexo == 1:
    saldo = 18 - idade
    print(f'ainda faltam {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento sera em {ano}')

elif idade > 18 and sexo == 1:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado a {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
elif sexo == 2:
    print('Para sexo feminino não é obrigatório se alistar!')
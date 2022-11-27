
from datetime import date

ano = date.today().year
pessoas = 8
for idade in range(1, pessoas):
    data = int(input('Digite sua data de nacimento: '))
    a = ano - data

    if  a > 18:
        print(a)
        print(f'O total de maiores de idade são {idade}' )

    elif a < 18:
        print(a)
        print(f'O total de menores de idade é de {idade}')
   
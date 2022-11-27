print('\033[1;33mx'*40,'TABUADA','X'*40)

tabuada = int(input('Digite a tabuada desejada: '))

for x in range(1, 11, 1):
   s = tabuada * x
   print(f'{tabuada}x{x}= {s}')

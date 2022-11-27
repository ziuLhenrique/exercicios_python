from time import sleep

print('\033[4;32m*'*40,'CONTAGEM REGRESSIVA!','*'*40)

for contagem in range(10, -1, -1):
    sleep(1)
    print(contagem)

print('FELIZ ANO NOVO!')
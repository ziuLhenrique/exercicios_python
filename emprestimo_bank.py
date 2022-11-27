casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salario: R$'))
anos = int(input('Quantos anos ira pagar?: '))

prestacao = casa / (anos*12)
minimo = salario * 30 / 100

if prestacao <= minimo:
    print('Empréstimo pode ser CONSEDIDO!')

else:
    print('Emprestimo NEGADO!')
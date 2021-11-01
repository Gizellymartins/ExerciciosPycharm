print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')

op = input('Qual operação deseja fazer? ')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

while (op != 's'):
        if (op == '+'):
            res = x + y
            print('Resultado: {} + {} = {}'.format(x, y, res))
        elif (op == '-'):
            res = x - y
            print('Resultado: {} - {} = {}'.format(x, y, res))
        elif (op == '*'):
            res = x * y
            print('Resultado: {} * {} = {}'.format(x, y, res))
        elif (op == '/'):
            res = x / y
            print('Resultado: {} / {} = {}'.format(x, y, res))
        else:
            print('Operação inválida!')

        op = input('Qual operação deseja fazer? ')
        if op == '+' or op == '-' or op == '*' or op == '/':
            x = int(input('Digite o primeiro valor: '))
            y = int(input('Digite o segundo valor: '))


print('Encerrando o programa...')

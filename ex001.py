nome = input('Qual seu nome?')
print('Bem vindo funcionario(a): {:=^20}'.format(nome))
print('Aumentos do mês, calcule seu novo sálario:')
n1 = float(input('Digite seu salário atual: '))
print('Esse mês seu salário tera um aumento de 15%')
n2 = 0.15
n3 = n2 * n1
print('Salário com aumento {} = '.format(n1+n3))

n=int(input('digite um número:'))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n,a,s))
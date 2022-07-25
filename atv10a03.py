#Escrever um algoritmo que calcule a média harmônica de três valores dada pela fórmula:

print('Calcular a média harmônica')
a = float(input('Digite o valor de a '))
b = float(input('Digite o valor de b '))
c = float(input('Digite o valor de c '))

mh= 3 / ((1/a)+(1/b)+(1/c))

print(f'A media harmônica de {a}, {b} e {c} é {mh:.3f}. ')
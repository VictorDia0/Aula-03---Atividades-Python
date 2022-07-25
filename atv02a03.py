# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considerando a cotação de 1 real = 5,15.

print('Abaixo escreva quanto de dinheiro você tem na carteira')
real =float(input('Digite o valor: '))
res = real / 5.15
print('Com {:.2f} reais, você pode comprar {:.2f} dolares' .format(real,res))
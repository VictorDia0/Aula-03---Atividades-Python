# Crie um programa que leia o preço de um produto de mostre o valor com 5% de desconto.

print('Digite o valor o produto que deseja calcular 5% de desconto.')
pro =float(input('Digite o valor do produto: '))
des =  pro * 0.95

print('Com 5% de desconto esse produto de R${:.2f} reais passará a valer R${:.2f} reais' .format(pro,des))
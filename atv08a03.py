#Faça um programa que receba hora e minutos, e calcule a hora digitada apenas em minutos.

horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))

print(f'A quantidade de horas convertidas em minutos é de {(horas * 60) + minutos} minutos')
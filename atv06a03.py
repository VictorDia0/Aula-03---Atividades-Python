#Faça um programa que receba o salário-base de um funcionário, calcule e mostre o salário a receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base, e paga imposto de 7% sobre o salário-base.

print('Cálculo do salário')
Sal= float(input('Informe o seu salário:'))
cal = (Sal * 0.93) * 1.05

print(f'Pagando o imposto e adcionando a gratificação o salário atual ficou de R$ {cal} reais')
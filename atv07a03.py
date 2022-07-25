#Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre a idade desta pessoa, e quantos anos essa pessoa terá em 2028.

anonasc = int(input('Digite o ano de nascimento: '))
anoatual = int(input('Digite o ano atual: '))

print(f'Você tem {anoatual - anonasc} anos, e em 2028 você terá {2028 - anonasc} anos.')

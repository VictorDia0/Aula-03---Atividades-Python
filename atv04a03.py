#Faça um programa que receba três notas e seus respectivos, pesos calcule e mostre a média ponderada entre essas notas.
nomealuno =str(input('Digite o nome do aluno desejado -'))
nota01 =float(input('Prova 01: '))
nota02 =float(input('Prova 02: '))
nota03 =float(input('Prova 03: '))
media =(nota01 + nota02 + nota03) / 3

print('Olá {}, sua nota nas provas 01, 02 e 03 foi de {}, {}, {}, logo sua media foi de {:.2f}' .format(nomealuno,nota01,nota02,nota03,media))
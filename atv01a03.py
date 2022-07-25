#Programa de percentual do preço da gasolina

print ('Abaixo descrea os valores da gasolina e o etanol')
gas = float (input('Preço da gasolina: '))
eta = float (input('Preço do etanol: '))
val = (eta / gas) * 100
if val < 70 :
    print('O valor é abaixo de {:.2f}%, então use álcool.' .format(val))
elif val > 70 :
    print('O valor é acima de {:.2f}%, então use Gasolina.' .format(val))
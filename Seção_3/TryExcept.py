#Introdução ao try except

numero = input('Vou dobrar o numero:')

try:
    num_float = float(numero)
    print(f'O dobro de {numero} é {num_float * 2:.1f}')
except:
    print('Isso não é um número')
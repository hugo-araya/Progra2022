i = 0
while i < 10:
    numero = int(input('Numero: '))
    if numero > 0:
        print('-----------> Positivo')
    else:
        if numero < 0:
            print('********** Negativo')
        else:
            print('++++++++++ Neutro')
    i = i + 1

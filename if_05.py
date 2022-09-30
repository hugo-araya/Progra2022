i = 0
posi = 0
nega = 0
neut = 0
while i < 5:
    numero = int(input('Numero: '))
    if numero > 0:
        posi = posi + 1
    else:
        if numero < 0:
            nega = nega + 1
        else:
            neut = neut + 1
    i = i + 1
print('Positivos: ', posi)
print('Negativos: ', nega)
print('Neutros  : ', neut)

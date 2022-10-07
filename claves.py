maestra = input('Clave maestra: ')
clave1 = ''
clave2 = ''
largo = len(maestra)
i = 0
while i < largo:
    digito = int(maestra[i])
    if digito%2 == 0:
        clave2 = clave2+str(digito)
    else:
        clave1 = clave1+str(digito)
    i = i + 1
print('Clave maestra:', maestra)
print('Clave1:', clave1)
print('Clave2:', clave2)

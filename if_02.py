i = 0
n = int(input('Cantidad: '))
while i < n:
    nota = float(input('Nota : '))
    suma = suma + nota
    i = i + 1
promedio = suma/n
print('Promedio: ', promedio)
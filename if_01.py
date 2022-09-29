hora_trabajada = float(input('Horas: '))
if hora_trabajada > 40:
    hora_extra = hora_trabajada - 40 
    sueldo = hora_extra * 2000 + 40 * 1600
else:
    sueldo = hora_trabajada * 1600
print('Sueldo: ',sueldo)


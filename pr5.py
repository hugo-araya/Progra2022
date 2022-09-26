p_interes = float(input('Ingrese porcentaje: '))
cap_inv = int(input('Capital a invertir: '))
saldo = cap_inv
interes_calculado = cap_inv * p_interes 
if interes_calculado > 7000:
    saldo = cap_inv + interes_calculado
print(saldo)
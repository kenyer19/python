'calcular y visualizar la longitud de la circunferencia y el area de un circulo de radio dado'
print ('calcular el area y la longitud de un circulo')

import math

radio = float(input('radio -'))
area = math.pi * radio**2 
longitud = 2 * math.pi * radio 

print (f'el area es = {area}')
print (f'la longitud de la circunferencia es = {longitud}')

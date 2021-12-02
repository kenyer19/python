
class figuras(object):
    def __init__(self,altura,base,radio,):
        self.altura=altura
        self.base=base
        self.radio=radio
    
       


class rectangulo(figuras):
    print ('no se puede calcular la figura')    
class cuadrado(figuras):
    print ('no se puede calcular la figura')   

class triangulo(figuras):
    print ('calcular la superficie del triangulo')
base = 5
altura = 2
superficie = (5* 2) / 2  
print ('la superficie del triangulo es:',superficie)

class circulo(figuras):
    print ('calcular el area y la longitud de un circulo')

import math

radio = 3
area = math.pi * 3**2
longitud = 2 * math.pi * 3

print (f'el area es = {area}')
print (f'la longitud de la circunferencia es = {longitud}')




    
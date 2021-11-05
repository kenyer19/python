#!/usr/bin/python3
frase = input("ingrese la frase: ")

frase = frase.lower()

vocales= ['a','e','i','o','u','á','é','í','ó','ú','A','E','I','O','U','Á','É','Í','Ó','Ú']

for x in vocales:
    veces=0
    for y in frase:
        if x==y:
            veces+=1


    print("la vocal", x ,"aparece", veces ,"veces")      


def contar_vocales(vocales,frase):
    veces=0
    for x in vocales:
        for y in frase:
            if x==y:
                veces+=1


    print('el numero de vocales es:',veces )   
    contar_vocales()




    

    

    

            

            


           



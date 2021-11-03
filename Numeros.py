#numeros pares 
inicio = 1
fin = 100
for i in range (inicio,fin,2):
    print (i +1)

#numeros impares
for i in range (inicio -2, fin -1, 2):
    print (i+2)

#numeros primos
for i in range (inicio +1, fin +1):
    primo =True
    if i == 2 or i == 3 or i ==5 or i == 7 or i == 11 or i ==13:
        print (i)
    if (i%2 !=0):
        if(i%3 !=0):
             if (i%5 !=0):
                 if(i%7 !=0):
                     if(i%11 !=0):
                         if (i%13 !=0):
                             print (i)

       

    

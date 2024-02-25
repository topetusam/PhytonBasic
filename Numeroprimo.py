Num1= int(input("ingrese el numero para saber si es primo :"))

elnumeroesprimo=True
        
    
if Num1 < 0:
    print("ingrese un numero positivo")

else:
    for i in range(2, Num1):
        if Num1%i==0:
            elnumeroesprimo=False                
            break
        
if elnumeroesprimo:
    print("el numero es primo") 
else:
    print("el numero no es primo")
        
               
            
        
    
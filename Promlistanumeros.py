Num1= int(input("Ingrese la cantidad de numeros que desea sacar su promedio"))

suma=0

for i in range(Num1):
    numero = int(input("Ingrese los numeros"))
    print("los numeros son,", [i+1], numero)
    
    suma = (suma+numero)
    

    
print("La suma de los numeros es  : ",suma)
       
print("El promedio de los numeros ingresados es : ", (suma/Num1))    
    
    

 
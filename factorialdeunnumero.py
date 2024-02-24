Num1 = int(input("ingrese el numero del cual desea el factorial : "))
factorial= 1

#el factorial solo se pude para numeros positivos
#el factrorial de 0 es 1 

if Num1 < 0:
    print("el numero no tiene factorial")
elif Num1 == 0:
    print("el factorial de 0 es 1")
else: 
    for i in range(1, Num1 + 1):
        factorial = factorial * i
    print("el factorial es :", factorial)
            
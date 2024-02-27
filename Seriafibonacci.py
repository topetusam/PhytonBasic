numero = 15
a,b = 0,1
print("serie fibonacci")
print(a)
print(b)

for i in range (2,numero):
    c = a+b
    print(c)
    a=b
    b=c
 
# numero perfectos de 1 a 500

n = int(input("ingrese el numero para encontrar el perfecto "))
i = 1
total=0
while (i <n):
    if n%i==0:
        total= total+i
    i=i+1
if total==n:
    print("el numero es perfecto") 
else:
    print("no es perfecto" )       
    
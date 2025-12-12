def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return  
a = int(input("Introdueixi un numero pero a fer el factorial")
print(factorial(a))
    










"""def sumaun(m):
    for i,e in enumerate(m):
        m[i]=e +1

l=[5, 6, 7, 10]
print(l)
sumaun(l)
print(l)
sumaun(l)
print(l)
"""



"""def ordenar(x, y):
    # Prec: donat dos numeros
    # Post: Retorn el menos i despres el major
    if x>y:
        return y, x
    elif y>x:
        return x, y
    else:
        return x, y 
    
# programa principal
v1 = int(input("Intro el 1r numero: "))
v2 = int(input("Intro el 2n numero: "))
v2, v1 = ordenar(v1, v2)
for e in range(v2, v1+1, 2):
    if e%2==1:
        print(e)
        """
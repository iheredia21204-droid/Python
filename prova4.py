a = [1,"a", "Capça", [2], 1, "a"]
for e in a:
    if a.count(e)>1:
        print(e)

"""a.ap
a.append("Cadena nova")
a.append([10, 11, 12])
a.extend([10, "Cadena nova", [10, 11, 12]])
print(a)
"""
for e in a:
    print(e)
for i in range(len(a)):
    a[i]*=2 # --> a[i]= a[i]*2
    print("La posició {} té el valor {}".format(i,a[i]))
for i,e in enumerate(a):
    print("La posició {} té el valor {}".format(i,e))
""
a = float(input("Escriure el primer nombre: "))
b = float(input("Escriure el primer segon nombre: "))
f= float(input("Escriure el primer tercer nombre: "))
c = a + b + f
print("El resultat de la suma {} + {} + {} és {}" .format(a, b, f, c))
if c>20:
    print("La suma és major que 20, que és {}".format(c))
else:
    print("La suma és menor que 20, que és {}".format(c))
c = a * b * f
print("El resultat de la multiplicació {} * {} * {} és {}".format (a, b, f, c))
if c>100:
    print("La multiplicació és major que 100, que és {}".format(c))
else:
    print("La multiplicació és menor que 100, que és {}".format(c))
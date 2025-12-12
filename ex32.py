# Definim la funció mostrar_majors_que
def mostrar_majors_que(tupla, x):
    print(f"Números superiors a {x}:")
    for num in tupla:
        if num > x:
            print(num)


# Programa principal
# Demanem quants números vol l'usuari
n = int(input("Quants números vols introduir a la tupla? "))

# Creem la tupla a partir dels inputs
numeros = tuple(int(input(f"Introdueix el número {i+1}: ")) for i in range(n))

# Mostrem els números superiors a 18
mostrar_majors_que(numeros, 18)
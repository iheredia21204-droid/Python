# Demanem dues paraules
paraula1 = input("Introdueix la primera paraula: ").lower()
paraula2 = input("Introdueix la segona paraula: ").lower()

# Comprovem la longitud mínima de 2 o 3 lletres
min_len = min(len(paraula1), len(paraula2))

# Inicialitzem el resultat
resultat = "No rimen"

# Comprovem coincidència de 3 últimes lletres
if min_len >= 3 and paraula1[-3:] == paraula2[-3:]:
    resultat = "Rimen"
# Comprovem coincidència de 2 últimes lletres
elif min_len >= 2 and paraula1[-2:] == paraula2[-2:]:
    resultat = "Rimen un poc"

# Mostrem el resultat
print(resultat)

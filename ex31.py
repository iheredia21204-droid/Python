# Demanem l'any actual
any_actual = int(input("Introdueix l'any actual: "))

# Creem llistes per noms i anys de naixement
noms = []
anys_naixement = []

# Demanem les dades de 4 persones
for i in range(4):
    nom = input(f"Nom de la persona {i+1}: ")
    any_naix = int(input(f"Any de naixement de {nom}: "))
    noms.append(nom)
    anys_naixement.append(any_naix)

# Imprimim les dades tabulades
print("\nNom\t\tData naixement\tAnys que farà aquest any")
for i in range(4):
    edat = any_actual - anys_naixement[i]
    print(f"{noms[i]:<12}{anys_naixement[i]}\t\t{edat}")

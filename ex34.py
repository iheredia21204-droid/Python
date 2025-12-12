def nums_que_comencen_per(llista, lletra):
    # Comptador per noms que comencen per la lletra donada
    comptador = 0
    for nom in llista:
        if nom.lower().startswith(lletra.lower()):
            comptador += 1
    return comptador


# Exemple d'ús
noms = ["Anna", "Albert", "Maria", "Àlex", "Pere", "ana"]

# Demanem la lletra a l'usuari
lletra = input("Introdueix la lletra per buscar: ")

# Comptem i mostrem el resultat
resultat = nums_que_comencen_per(noms, lletra)
print(f"Hi ha {resultat} noms que comencen per la lletra '{lletra}'.")

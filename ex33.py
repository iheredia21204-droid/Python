def nums_que_comencen_per(llista, lletra='a'):
    # Comptador per noms que comencen per la lletra donada
    comptador = 0
    for nom in llista:
        if nom.lower().startswith(lletra.lower()):
            comptador += 1
    return comptador


# Exemple d'ús
noms = ["Anna", "Albert", "Maria", "Àlex", "Pere", "ana"]
resultat = nums_que_comencen_per(noms)
print(f"Hi ha {resultat} noms que comencen per la lletra 'a'.")

def crear_llista_fitxer(nom_fitxer):
    """
    Llegeix un fitxer i retorna una llista amb cada paraula com un element.
    """
    llista_paraules = []
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            for linia in fitxer:
                # Separem la línia en paraules i les afegim a la llista
                paraules = linia.strip().split()
                llista_paraules.extend(paraules)
        return llista_paraules
    except FileNotFoundError:
        print(f"El fitxer '{nom_fitxer}' no existeix.")
        return []

# Exemple d'ús
nom_fitxer = "exemple.txt"  # Substitueix pel teu fitxer
llista = crear_llista_fitxer(nom_fitxer)
print("Llista de paraules llegides del fitxer:")
print(llista)

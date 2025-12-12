def llegir_fitxer(nom_fitxer):
    """
    Llegeix el contingut d'un fitxer i el retorna com a llista de línies.
    Si el fitxer no existeix o hi ha un error d'obertura, mostra un avís i retorna una llista buida.
    """
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            contingut = fitxer.readlines()  # Llegeix totes les línies
        return contingut
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        return []
    except IOError:
        print(f"Error: Hi ha hagut un problema en obrir el fitxer '{nom_fitxer}'.")
        return []

# Prova
nom_fitxer = "exemple.txt"
linies = llegir_fitxer(nom_fitxer)

if linies:
    print("Contingut del fitxer:")
    for linia in linies:
        print(linia.strip())

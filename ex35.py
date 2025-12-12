def comptar_vocals(paraula):
    # Inicialitzem un diccionari per comptar cada vocal
    vocals = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Recorrem cada lletra de la paraula
    for lletra in paraula.lower():
        if lletra in vocals:
            vocals[lletra] += 1
    
    # Mostrem el resultat
    for v, compt in vocals.items():
        print(f"{compt} {v}'s")

# Exemple d'ús
comptar_vocals("Ratapinyada")

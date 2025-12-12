def esta_ordenada(llista):
    """
    Retorna un missatge indicant si la llista està ordenada
    de manera ascendent, descendent o no està ordenada.
    """
    if llista == sorted(llista):
        return "Està ordenada de forma ascendent"
    elif llista == sorted(llista, reverse=True):
        return "Està ordenada de forma descendent"
    else:
        return "No està ordenada"

# Proves
print(esta_ordenada([3, 2, 1]))       # Està ordenada de forma descendent
print(esta_ordenada([4, 5, 6]))       # Està ordenada de forma ascendent
print(esta_ordenada([1, 3, 2, 4]))    # No està ordenada
print(esta_ordenada([10]))            # Està ordenada de forma ascendent (únic element)

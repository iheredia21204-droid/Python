def gran_llista(llista):
    # Comprovem que la llista no estigui buida
    if not llista:
        return None  # o es pot llençar un error
    
    # Inicialitzem el màxim amb el primer element
    maxim = llista[0]
    
    # Recorrem la llista buscant el major
    for num in llista:
        if num > maxim:
            maxim = num
    return maxim

# Proves
print(gran_llista([3, 4, 2, 3, 10]))  # Retorna 10
print(gran_llista([-1, -5, -2]))      # Retorna -1
print(gran_llista([7]))               # Retorna 7

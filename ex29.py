def comptar_majuscules(cadena):
    comptador = 0
    for lletra in cadena:
        if lletra.isupper():   # Comprova si la lletra és majúscula
            comptador += 1
    return comptador


# Proves
print(comptar_majuscules("Hola Mundo"))          # Retorna 2 (H, M)
print(comptar_majuscules("Python ES Genial"))    # Retorna 4 (P, E, S, G)
print(comptar_majuscules("sense majuscules"))    # Retorna 0
print(comptar_majuscules("TOT EN MAJUSCULES"))   # Retorna 17

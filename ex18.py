def ex18(c):
    v = "aeiouAEIOUáàéèíìóòúùÁÀÉÈÍÌÓÒÚÙ"
    if c in v:
        return True
    else:
        return False

# Programa principal
c = input("Escriu un caracter per a provar si es o no una vocal:")
print(ex18(c))
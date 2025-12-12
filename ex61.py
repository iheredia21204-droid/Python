def lenp(frase):
    """
    Retorna una llista amb la longitud de cada paraula de la frase.
    """
    paraules = frase.split()  # Separem la frase en paraules
    longituds = list(map(len, paraules))  # Apliquem len a cada paraula
    return longituds

# Proves
frase1 = "Hola com estàs"
frase2 = "Aquest és un exemple de frase"

print(lenp(frase1))  # Retorna [4, 3, 5]
print(lenp(frase2))  # Retorna [6, 2, 2, 7, 2, 5]

def es_palindrom(paraula):
    """
    Retorna True si la paraula és un palíndrom, False en cas contrari.
    """
    paraula = paraula.lower().replace(" ", "")   # ignorem majúscules i espais
    return paraula == paraula[::-1]

# Exemples de prova
print(es_palindrom("radar"))     # True
print(es_palindrom("civic"))     # True
print(es_palindrom("Rallar"))    # True
print(es_palindrom("Hola"))      # False
print(es_palindrom("Soc del Ramis"))  # False

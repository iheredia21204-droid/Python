def lletres_paraula(paraula):
    """
    Retorna una llista amb les lletres de la paraula donada.
    """
    return [lletra for lletra in paraula]

# Proves
paraula = "institut"
print(lletres_paraula(paraula))
# Retorna ['i', 'n', 's', 't', 'i', 't', 'u', 't']

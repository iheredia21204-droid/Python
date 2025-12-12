def concatena_llistes(llista1, llista2, connector):
    """
    Concatena dues llistes element a element amb un connector.
    """
    return [a + connector + b for a, b in zip(llista1, llista2)]

# Proves
llista1 = ['sub', 'supra']
llista2 = ['campió', 'campiona']
connector = '-'

print(concatena_llistes(llista1, llista2, connector))
# Retorna ['sub-campió', 'supra-campiona']

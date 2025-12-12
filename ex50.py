import random

def llista_20_elements():
    """
    Retorna una llista de 20 elements aleatoris entre 1 i 100.
    """
    return [random.randint(1, 100) for _ in range(20)]

def hi_ha_duplicats(llista):
    """
    Retorna True si hi ha duplicats a la llista, False en cas contrari.
    """
    return len(llista) != len(set(llista))

# Generem la llista
llista = llista_20_elements()
print("Llista generada:", llista)

# Comprovem si hi ha duplicats
if hi_ha_duplicats(llista):
    print("Hi ha elements duplicats a la llista.")
else:
    print("No hi ha elements duplicats a la llista.")

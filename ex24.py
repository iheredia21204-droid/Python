def crear_punts(llista):
    """
    Mostra per pantalla tants punts com indiqui cada número de la llista.
    Cada element de la llista es mostra en una línia separada.
    """
    for n in llista:
        print("." * n)

# Exemple de prova
crear_punts([2, 3, 4])
# Sortida:
# ..
# ...
# ....

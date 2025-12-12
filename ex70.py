def dividir(a, b):
    """
    Retorna el resultat de a / b. Si b és zero, mostra un avís i retorna None.
    """
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        print("Error: No es pot dividir per zero!")
        return None

# Proves
print(dividir(10, 2))   # Retorna 5.0
print(dividir(5, 0))    # Mostra l'avís i retorna None

def sumar_llista(llista):
    """
    Suma todos los valores de una lista.
    """
    suma = 0
    for x in llista:
        suma += x
    return suma


def multiplicar_llista(llista):
    """
    Multiplica todos los valores de una lista.
    """
    producte = 1
    for x in llista:
        producte *= x
    return producte


# Ejemplos de prueba
print(sumar_llista([1, 2, 3, 4]))        # 10
print(multiplicar_llista([1, 2, 3, 4])) # 24

print(sumar_llista([5, 5, 5]))          # 15
print(multiplicar_llista([5, 5, 5]))    # 125

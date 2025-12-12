def gran(a, b):
    """
    Devuelve el número mayor entre a y b.
    """
    if a > b:
        return a
    else:
        return b

# Pruebas con diferentes ejemplos
print(gran(5, 10))
print(gran(-3, -7))
print(gran(8, 8))
print(gran(0, 42))

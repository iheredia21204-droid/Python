def numeros_elevats_a_potencia(n, potencia):
    """
    Retorna una llista dels n primers números elevats a la potència indicada.
    """
    return [i ** potencia for i in range(n)]

# Proves
print(numeros_elevats_a_potencia(10, 2))  # Quadrats: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(numeros_elevats_a_potencia(10, 3))  # Cubes: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

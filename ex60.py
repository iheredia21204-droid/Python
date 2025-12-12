def es_primer(n):
    """Retorna True si n és primer, False en cas contrari."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Llista per guardar els nombres primers
primers = []

# Comprovem els nombres de 1 a 100
for num in range(1, 101):
    if es_primer(num):
        primers.append(num)

# Mostrem els nombres primers
print("Nombres primers entre 1 i 100:")
print(primers)

# Mostrem la quantitat de nombres primers
print(f"Hi ha {len(primers)} nombres primers entre 1 i 100.")

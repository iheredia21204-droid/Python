from functools import reduce

def Passar_a_Numero(llista):
    """
    Retorna el número corresponent a una llista de dígits.
    Ex: [3,4,1,5] -> 3415
    """
    return reduce(lambda x, y: x * 10 + y, llista)

# Proves
digits1 = [3, 4, 1, 5]
digits2 = [1, 0, 2, 5]

print(Passar_a_Numero(digits1))  # Retorna 3415
print(Passar_a_Numero(digits2))  # Retorna 1025

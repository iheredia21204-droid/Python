def hi_ha_duplicats(llista):
    """
    Retorna True si hi ha algun element duplicat a la llista, False en cas contrari.
    """
    return len(llista) != len(set(llista))  # Converteix a set per eliminar duplicats i compara longitud

# Proves
print(hi_ha_duplicats([1, 2, 3, 4, 5]))      # False, cap duplicat
print(hi_ha_duplicats([1, 2, 2, 3, 4]))      # True, el 2 es repeteix
print(hi_ha_duplicats(['a', 'b', 'c']))      # False
print(hi_ha_duplicats(['a', 'b', 'a']))      # True

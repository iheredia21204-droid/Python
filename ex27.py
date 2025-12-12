def paraula_mes_llarga(llista):
    # Comprovem que la llista no estigui buida
    if not llista:
        return None

    # Inicialitzem amb la primera paraula
    mes_llarga = llista[0]

    # Recorrem la resta per trobar la més llarga
    for paraula in llista:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula

    return mes_llarga


# Proves
print(paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))  # Retorna: Paraula
print(paraula_mes_llarga(["cotxe", "avió", "bicicleta"]))       # Retorna: bicicleta
print(paraula_mes_llarga(["a"]))                                # Retorna: a

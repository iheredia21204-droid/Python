def paraules_per_lletra(llista, lletra):
    """
    Retorna una llista amb les paraules que comencen per la lletra donada.
    """
    # Converteix la lletra a minúscula per evitar errors de majúscules/minúscules
    lletra = lletra.lower()
    # Filtra les paraules que comencen per la lletra
    return list(filter(lambda paraula: paraula.lower().startswith(lletra), llista))

# Proves
llista_paraules = ["maria", "manta", "peu", "mà"]
print(paraules_per_lletra(llista_paraules, 'p'))  # Retorna ['peu']
print(paraules_per_lletra(llista_paraules, 'm'))  # Retorna ['maria', 'manta', 'mà']

def dibuixar_imatge():
    """
    Dibuixa una imatge utilitzant punts per línies.
    """
    llista_valors = [1, 3, 5, 7, 9]
    crear_punts(llista_valors)

def crear_punts(llista):
    for n in llista:
        print("." * n)

# Llamada correcta
dibuixar_imatge()

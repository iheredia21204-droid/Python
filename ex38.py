import random

def generar_codi():
    """Genera un codi aleatori de 4 dígits del 0 al 9."""
    codi = [str(random.randint(0, 9)) for _ in range(4)]
    return codi

def verificar_jugada(codi_secret, codi_usuari):
    """
    Comprova la jugada de l'usuari.
    Retorna:
    - encerts: nombre de dígits correctes en la posició correcta
    - coincidencies: nombre de dígits correctes però en la posició incorrecta
    """
    encerts = 0
    coincidencies = 0

    # Copiï dels codis per poder manipular-los
    codi_secret_rest = []
    codi_usuari_rest = []

    # Primer comptem els encerts (mateixa posició)
    for i in range(4):
        if codi_usuari[i] == codi_secret[i]:
            encerts += 1
        else:
            codi_secret_rest.append(codi_secret[i])
            codi_usuari_rest.append(codi_usuari[i])

    # Ara comptem les coincidències (mateix número però posició diferent)
    for num in codi_usuari_rest:
        if num in codi_secret_rest:
            coincidencies += 1
            codi_secret_rest.remove(num)  # Evita comptar dues vegades

    return encerts, coincidencies

def jugar_mastermind():
    print("Benvingut a MasterMind simplificat!")
    print("El codi secret té 4 dígits del 0 al 9.")
    print("Introdueix codis de 4 dígits fins que l'endevinis.\n")

    codi_secret = generar_codi()
    intents = 0

    while True:
        codi_usuari = input("Introdueix un codi de 4 dígits: ")
        if len(codi_usuari) != 4 or not codi_usuari.isdigit():
            print("Codi invàlid. Ha de ser exactament 4 dígits.")
            continue

        intents += 1
        encerts, coincidencies = verificar_jugada(codi_secret, list(codi_usuari))

        if encerts == 4:
            print(f"Felicitats! Has endevinat el codi {''.join(codi_secret)} en {intents} intents.")
            break
        else:
            print(f"{encerts} encerts en la posició correcta, {coincidencies} coincidències en posició incorrecta.\n")

# Inici del joc
jugar_mastermind()

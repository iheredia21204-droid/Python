def filtrar_paraules(llista, x):
    # Retorna una nova llista amb les paraules que tenen més de x caràcters
    resultat = []
    for paraula in llista:
        if len(paraula) > x:
            resultat.append(paraula)
    return resultat


# Proves
print(filtrar_paraules(["Hola", "Ramis", "IES", "Paraula"], 3))  
# Retorna: ['Hola', 'Ramis', 'Paraula']

print(filtrar_paraules(["cotxe", "avió", "bicicleta"], 5))      
# Retorna: ['bicicleta']

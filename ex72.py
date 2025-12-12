import os

# 1. Crear el directori /home/cicles/AO/Prova si no existeix
directori = "/home/cicles/AO/Prova"
os.makedirs(directori, exist_ok=True)

# 2. Canviar al directori creat
os.chdir(directori)

# 3. Crear el fitxer Ex12.txt i afegir els noms dels companys
companys = ["Anna", "Pere", "Maria", "Joan"]  # Substitueix amb els noms reals
with open("Ex12.txt", "w", encoding="utf-8") as fitxer:
    for nom in companys:
        fitxer.write(nom + "\n")

# 4. Obrir el fitxer per afegir els noms dels professors
professors = ["Sr. Ramis", "Sra. Puig"]  # Substitueix amb els noms reals
with open("Ex12.txt", "a", encoding="utf-8") as fitxer:
    for nom in professors:
        fitxer.write(nom + "\n")

# 5. Obrir el fitxer i posar tot el contingut dins d'una llista
with open("Ex12.txt", "r", encoding="utf-8") as fitxer:
    llista_noms = [linia.strip() for linia in fitxer]

# 6. Mostrar la llista final
print(llista_noms)

from abc import ABC, abstractmethod

# Classe base Animal amb mètodes abstractes
class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        print(f"{self.especie} fa un so típic del quisoc")

# Subclasses
class Cavall(Animal):
    def xerrar(self):
        print("Cavall: Iiiiih!")

    def mourem(self):
        print("Cavall: Galopant!")

class Dofi(Animal):
    def xerrar(self):
        print("Dofí: Klik-klik!")

    def mourem(self):
        print("Dofí: Nedant!")

class Abella(Animal):
    def xerrar(self):
        print("Abella: Bzzz!")

    def mourem(self):
        print("Abella: Volant!")

    def picar(self):
        print("Abella: Pica!")

class Human(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        print(f"{self.nom} diu: Hola!")

    def mourem(self):
        print(f"{self.nom} camina!")

class Fiet(Human):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares  # Llista de noms dels pares

    def nompares(self):
        print(f"Els pares de {self.nom} són: {', '.join(self.pares)}")

class Centaure(Cavall, Human):  # Herència múltiple
    def __init__(self, especie, edat, nom):
        Cavall.__init__(self, especie, edat)
        self.nom = nom

    def xerrar(self):
        print(f"Centaure {self.nom}: Hiii i Hola!")

    def mourem(self):
        print(f"Centaure {self.nom}: Galopant i caminant alhora!")

# Classe sense relació amb Animal però amb els mateixos mètodes
class Xou:
    def xerrar(self):
        print("Xou: Fa soroll!")

    def mourem(self):
        print("Xou: Es mou!")

    def quisoc(self):
        print("Xou: Soroll de quisoc!")

# Crear una llista d'elements de cada tipus
elements = [
    Cavall("Cavall", 5),
    Dofi("Dofí", 3),
    Abella("Abella", 1),
    Human("Humà", 30, "Maria"),
    Fiet("Humà", 5, "Joanet", ["Maria", "Joan"]),
    Centaure("Centaure", 40, "Centauri"),
    Xou()
]

# Bucle que crida als mètodes iguals
for elem in elements:
    elem.xerrar()
    elem.mourem()
    elem.quisoc()
    if isinstance(elem, Abella):
        elem.picar()
    if isinstance(elem, Fiet):
        elem.nompares()
    print("-" * 30)

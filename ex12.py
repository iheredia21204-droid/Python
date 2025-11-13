def majoredat(edat):
    if edat > 18:
        print("Es major d'edat")
    elif edat<18:
        print ("Es menor d'edat")
    else:
        print("Enhorabona, aquest any has fet 18 anys")
        
edat = int(input("Escriure la seva edat: "))
majoredat(edat)
edat = int(input("Escriure la seva edat: "))
majoredat(edat)
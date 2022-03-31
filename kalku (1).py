import math
#kalkulaator
#NB!: Et kasutada valemeid või teoreemi vajuta "ENTER"
#NB!: Kalkulaatori kasutamisekas trüki "kalku"
kalk = input("Mis valemit või teoreemi tahate kasutada või kalkulaator? :")

if kalk=="kalku":
    klavar = input("1(liitmine) 2(lahutamine) 3(korrutamine) 4(jagamine): ") #Numbrid tähistavad varianti
    
    if klavar=="1":
        x = int(input("a = "))
        y = int(input("b = "))
        print(x+y)
        
    elif klavar=="2":
        x = int(input("a = "))
        y = int(input("b = "))
        print(x-y)
        
    elif klavar=="3":
        
        x = int(input("a = "))
        y = int(input("b = "))
        print(x*y)
    else:
        x = int(input("a = "))
        y = int(input("b = "))
        print(x/y)
        
else:
    var = input("(pythagorase teoreem, kiiruse valem, pindala, ruumala): ")
    #NB!:pythagorase teoreemi kasutamiseks trüki "pythagorase teoreem", "pythagorase" või "pyth"
    #NB!:kiiruse valemi kasutamisek trükki "kiiruse valem" või "kiiruse"
    if var=="pythagorase teoreem" or var=="pythagorase" or var=="pyth":
        kat = int(input("a = ")) #NB!:Kui ei ole arvu, siis trükki 0
        kat2 = int(input("b = "))
        hyp = int(input("c = "))
        
        if kat == 0:
            x = ((hyp**2) - (kat2**2))
            y = math.sqrt(x)
            print("a = " + str(y))
            
        elif kat2 == 0:
            x = ((hyp**2) - (kat**2))
            y = math.sqrt(x)
            print("b = " + str(y))
            
        elif hyp == 0:
            x = ((kat**2) + (kat2**2))
            y = math.sqrt(x)
            print("c = " + str(y))
        
    elif var == "kiiruse valem" or var =="kiiruse":
        v = int(input("Sisestage kiirus: "))
        s = int(input("Sisestage vahemaa (m): "))
        t = int(input("Sisestage aeg (sec): "))
        
        if v == 0:
            arv = float(s / t)
            
            print("Kiirus on " + str(arv) + "m/s")
            
        elif s == 0:
            arv = float(v * t)
            
            print("Vahemaa on " + str(arv) + "m")
            
        elif t == 0:
            arv = float(s / v)
            
            print("Aeg on " + str(arv) + "s")
            
    elif var == "pindala":
        kuj = input("Mis kuju pindala tahate arvutada?: ")
        
        if kuj == "ring":
            r = int(input("raadius = "))
            S = float(3.14 * (r**2))
            
            print("S = " + str(S))
            
        elif kuj == "ruut":
            a = int(input("külje pikkus = "))
            S = float(a**2)
            
            print("S = " + str(S))
        
        elif kuj == "ristkülik":
            a = int(input("külje pikkus = "))
            b = int(input("külje teise pikkus = "))
            S = float(a*b)
            
            print("S = " + str(S))
            
        elif kuj == "kolmnurk":
            a = int(input("alus = "))
            h = int(input("kõrgus = "))
            S = float((a*h) / 2)
            
            print("S = " + str(S))
            
        elif kuj == 'korrapärane hulknurk' or kuj == 'K.H':
            n = int(input('Sisestage tippude arv n = '))
            a = int(input('Sisestage küljede pikkus a = '))
            r = (math.sqrt(3) / 2) * a
            
            S = float((n * a * r) / 2)
            
            print("S = " + str(S))
            
    elif var == 'ruumala':
        kuj = input("Mis kuju ruumala tahate arvutada?: ")
        
        if kuj == "kera":
            r = int(input("raadius = "))
            V = float(4 / 3 * (r**3))
            
            print("V = " + str(V))
            
        elif kuj == "kuup":
            a = int(input("külje pikkus = "))
            V = float(a**3)
            
            print("V = " + str(V))
        
        elif kuj == "risttahukas":
            a = int(input("külje pikkus = "))
            b = int(input("külje teise pikkus = "))
            c = int(input("külje kolmanda pikkus = "))
            V = float(a * b * c)
            
            print("V = " + str(V))
            
        elif kuj == "püramiid":
            a = int(input("külje pikkus = "))
            n = int(input("alus nurkade arv = "))
            H = int(input("kõrgus = "))
            r = (math.sqrt(3) / 2) * a
            
            S = float((n * a * r) / 2)
            
            V = float((S * H / 3))
            
            print("V = " + str(V))
            
        elif kuj == 'silinder':
            r = int(input('Sisestage raadius r = '))
            h = int(input('Sisestage kõrgus h = '))
            
            V = float((3.14 * (r**2)) * h)
            
            print("V = " + str(V))
            
        elif kuj == 'koonus':
            r = int(input('Sisestage raadius r = '))
            h = int(input('Sisestage kõrgus h = '))
            
            V = float(((3.14 * (r**2)) * h) / 3)
            
            print("V = " + str(V))
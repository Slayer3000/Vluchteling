while True:
    print("Het verhaal van Ji-hoon")
    print ("Ji-Hoon, op 8 april 1993 geboren in Wonsan Noord-Korea ")
    print ("Op 9 December 2019 besluit hij om te vluchten van Noord-Korea.")
    print ("Hij stopt een rugtas vol met voedsel en kleren en gaat waar naar toe?")

    print ("A: Hij gaat via Zuid-Korea")
    print("B: hij gaat via China")

    devideone = input()
   
    if devideone == "A" or devideone == "a":
        print ("...")
        print ("Ji-Hoon pakt een taxi naar de DMZ")
        print ("Ji-Hoon moet nog 2 kilometers lopen. Zal hij via de weg of een zandpad gaan?")
        print ("A: de weg")
        print ("B: de zandweg")

        devide12 = input()
        if devide12 == "B" or devide12 == "b":
            print ("...")
            print ("Ji-hoon neemt de zandweg")
            print ("De beveiliging langs de zandweg is minimaal, dus hij ontsnapt naar Zuid-Korea.")
            print ("...")
            print ("...")
            print ("...")
            print ("Ji-hoon komt aan in Zuid-Korea. Hij wordt geholpen door de Zuid-Koreaanse overheid en leeft een lang en gelukkig leven in Zuid-Korea.")
            exit


        elif devide12 == "A" or devide12 == "a":
            print ("Ji-hoon kon niet ontsnappen")
            exit

    elif devideone == "B" or devideone == "b":
        print ("...")
        print ("Ji-hoon besluit naar china te gaan. Hij neemt de bus naar een plaatsje 10km van de grens af.")
        print ("Hoe zal hij over de grens komen?")
        print ("A: verstoppen in een toeristen bus.")
        print ("B: Op de voet")

        devidetwo = input()

        if devidetwo == "A" or devidetwo == "a":
            print ("...")
            print ("Ji-Hoon verstopt zichzelf in een bus")
            print ("Na lang wachten komt Ji-Hoon aan in Changchun, China")
            print ("China heeft een afspraak met Noord-Korea dat vluchtelingen terug worden gezonden")
            print ("Dus Ji-hoon heeft 2 opties.")
            print ("A: Vluchten naar Dalian")
            print ("B: Vluchten naar Mongolië")

            devidethree = input()

            if devidethree == "A" or devidethree == "a":
                print ("Ji-hoon komt aan in Dalian.")
                print ("Ji-hoon vindt een Japans schip en wordt verstopt aanboord.")
                print ("...")
                print ("Ji-hoon komt aan in Kumamoto, Japan")
                print ("Ji-hoon wordt in Japan geholpen en is ontkomen aan Noord-Korea")
                exit

            elif devidethree == "B" or devidethree == "b":
                print ("...")
                print ("Ji-Hoon besluit naar Mongolië te rijzen")
                print ("Hij neemt...?")
                print ("A: De Trein")
                print ("B: Het vliegtuig")

            devidefour = input()

            if devidefour == "A" or devidefour == "a":
                 print("...")
                 print("Ji-hoon pakt de trein naar Ulaanbataar, Mongolië")
                 print("In Mongolië wordt hij geholpen en leeft lang en gelukkig.")
                 exit

            elif devidefour == "B" or devidefour == "b":
                print ("...")
                print ("Ji-hoon komt aan op Internationaale Luchthaven Changchun Longjia.")
                print ("Ji-hoon komt echter niet door de duane heen en wordt terug gestuurd naar Noord-Korea")
                exit


        elif devidetwo == "A" or devidetwo == "a":
            print ("...")
            print("Na 10km lopen wordt Ji-hoon bij de grens opgepakt.")
            exit
            


        

import random

x = random.randint(1, 100) #x a szám amire gondol
y = 0 #y a szám amit tippelni fogsz, ha nem adom meg itt undefined error lesz a whileban
c = 0 #ez számlál

#Ha ezeket nem határozom meg előre nem fog működni, ez lehet az én korlátom csak.

#print(x) #Ha csalni akarsz leveszed a #t róla.

def kitalalom_a_szamot(talald_ki, aktualis_tipp, hanyadik_tipp):
    #talald_ki = random.randint(1, 100)  # x a szám amire gondol
    #aktualis_tipp = 0  # y a szám amit tippelni fogsz, ha nem adom meg itt undefined error lesz a whileban
    #hanyadik_tipp = 0  # ez számlál
    print("\nGondoltam egy természetes számra ami legfeljebb 100.\nKitalálod melyik az, legfeljebb 8 próbálkozásból?\n\nTippelj: ", end="")

    while aktualis_tipp != talald_ki and hanyadik_tipp < 8:
        hanyadik_tipp += 1
        aktualis_tipp = int(input())
        if aktualis_tipp == 78125:
            aktualis_tipp = talald_ki #cheatcode ami megnyeri a játátékot =5 * 5 * 5 * 5 * 5 * 5 * 5
            #print(y)
            #print(x)
        if aktualis_tipp == 279936:
            print(talald_ki) #cheatcode ami kiírja a helyes választ =6 * 6 * 6 * 6 * 6 * 6 * 6
        #megoldandó: ha cheatcodeot ír be valaki ne fusson hibára szerk: megoldva
            hanyadik_tipp -= 1

        if (aktualis_tipp < 1 or aktualis_tipp > 100) ^ (aktualis_tipp == 279936):
            raise ValueError("\nCsak 1-től 100-ig terjedő természetes számot tudok elfogadni.")
        # ha jól értem most ez úgy gondolkozik hogy
        # ha y kissebb mint 1 vagy y nagyobb mint 100 akkor A igaz
        # ha y == 279936 akkor a B igaz
        # tehát a XOR azt csinálja hogyha 279936 akkor az amúgy igaz A-t mi szerint nagyobb mint 100 hamisra állítja mert mindkettő nem lehet igaz
        # and not(-al is működik csak több karakter
        if aktualis_tipp == talald_ki: print("\nBizony! A szám nem más mint:", talald_ki)
        else:
            print(f"\nSajnos a számod ({aktualis_tipp}) nem egyenlő azzal amire gondoltam.\n")
            if hanyadik_tipp < 8:
                print("De nyugodtan újra próbálhatod!\nAdok egy tippet...\n")
            if talald_ki < aktualis_tipp:
               print("A szám amire gondoltam, kisebb mint: ", end="")
               print(aktualis_tipp)
            else:
               print("A szám amire gondoltam, nagyobb mint: ", end="")
               print(aktualis_tipp)
        if hanyadik_tipp < 8 and talald_ki != aktualis_tipp: print("Akkor most próbáld újra: ", end="")


    if hanyadik_tipp == 8 and aktualis_tipp != talald_ki:
        print("\nSajnálom, elfogytak a próbálkozásaid. : - (")
        print("Najó megsúgom ez volt: ", talald_ki, "\nAzért köszi a játékot! ^^")
    else:
        print("\nSikerült kitalálnod alig", end=" ")
        print(hanyadik_tipp, end =" ")
        print("próbálkozásból!\nKöszi a játékot! ^^")

    #Ez meglepően egyszerű volt (a xorig az már nem), majd folytatom azzal, hogy felajánlja, hogy melyikőtök találjon ki számot és kitalálja a számod a valószínűleg leggyorsabban.

#def talald_ki_a_szamot(x, y, c):

def talald_ki_a_szamot():
    print("Egytől százig mondhatsz egy számot, írd be, nem fogok lesni: ", end="")
    y = int(input())
    if y < 1 or y > 100: raise ValueError("\nTényleg nem lestem, de ez a szám szabálytalan!")

    x = random.randint(40, 60)

    while not(x == y):
        c += 1
        print(f"A szám amire gondoltál lehet hogy...{x}?\nÍrd be, hogy 1 ha igen, 2 ha nem.")
        igennem = int(input())
        if igennem == 1 and x == y: print("Szuper! "
        #to be continued







#kitalalom_a_szamot(x, y, c) #ideiglenesen kikapcsolva
talald_ki_a_szamot()
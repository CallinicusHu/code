import random

x = random.randint(0, 100) #x a szám amire gondol
y = 0 #y a szám amit tippelni fogsz, ha nem adom meg itt undefined error lesz a whileban
c = 0 #ez számlál

#Ha ezeket nem határozom meg előre nem fog működni, ez lehet az én korlátom csak.

#print(x) #Ha csalni akarsz leveszed a #t róla.

print("\nGondoltam egy természetes számra ami legfeljebb 100.\nKitalálod melyik az?\n\nTippelj: ", end="")

while y != x:
    y = int(input())
    if y == 78125:
        y = x #cheatcode ami megnyeri a játátékot =5 * 5 * 5 * 5 * 5 * 5 * 5
        #print(y)
        #print(x)
    if y == 279936: print(x) #cheatcode ami kiírja a helyes választ =6 * 6 * 6 * 6 * 6 * 6 * 6
    #megoldandó: ha cheatcodeot ír be valaki ne fusson hibára

    if (y < 1 or y > 100) ^ (y == 279936): raise ValueError("\nCsak 1-től 100-ig terjedő természetes számot tudok elfogadni.")
    # ha jól értem most ez úgy gondolkozik hogy
    # ha y kissebb mint 1 vagy y nagyobb mint 100 akkor A igaz
    # ha y == 279936 akkor a B igaz
    # tehát a XOR azt csinálja hogyha 279936 akkor az amúgy igaz A-t mi szerint nagyobb mint 100 hamisra állítja mert mindkettő nem lehet igaz
    if y == x: print("\nBizony! A szám nem más mint:", x)
    else:
        print("\nSajnos a számod (", end="")
        print(y, end="") #valamiért kénytelen voltam több sorba írni, nem engedte hogy egybekössem, de lehet csak elírtam valamit.
        print(") nem egyenlő azzal amire gondoltam.\nDe nyugodtan újra próbálhatod!\nAdok egy tippet:\n")
        if x < y:
           print("A szám amire gondoltam, kisebb mint: ", end="")
           print(y)
        else:
           print("A szám amire gondoltam, nagyobb mint: ", end="")
           print(y)
        print("Akkor most próbáld újra: ", end="")
    c += 1

print("\nSikerült kitalálnod alig", end=" ")
print(c, end =" ")
print("próbálkozásból!")

#Ez meglepően egyszerű volt, majd folytatom azzal, hogy felajánlja, hogy melyikőtök találjon ki számot és kitalálja a számod a valószínűleg leggyorsabban.

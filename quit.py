poging = 0
exitcode = ""
aantalHerhalingen = 0
while exitcode != "quit":
    aantalHerhalingen = aantalHerhalingen + 1
    exitcode = input("Typ quit om te stoppen ")
    poging += 1
    if exitcode != "quit":
        print("Aantal pogingen =", poging)
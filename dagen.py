dag = input("Welke dag? (ma,di,wo,do,vr,za,zo)").lower()
dagenlijst = ["ma", "di", "wo", "do", "vr", "za", "zo"]
printed_day = "None"
dagnummer = 0

while dag != printed_day:
    if dag in dagenlijst:
        print("")
    else:
        print("Kies een bestaande dag alstublieft.")
        break
    printed_day = dagenlijst[dagnummer]
    print(printed_day)
    dagnummer = dagnummer + 1
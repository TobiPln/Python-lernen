#float = Kommazahl -> 1.15
#int = Ganzzahl -> 1
#String = Text -> "Hallo"
#Bool = Wahr/Falsch -> true


print("Herzlich Willkommen zum Währungsrechner! ")
print("")
euro = input("Bitte Betrag in Euro eingeben: ")
dollar = 1.15 * float(euro)
print(f"Der Betrag entspricht {dollar} Dollar ")
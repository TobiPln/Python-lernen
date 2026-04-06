absender = input("Wer ist der Absender? ")


def generate_newsletter(absender):
    empfänger = input("An wem geht die Nachricht? ")
    print(f"Hallo {empfänger}")
    print("")
    print("Mit dieser Email möchte ich dich über meine neue Adresse informieren.")
    print("")
    print("Ponyhof 123")
    print("12345 Papayaland")
    print("Viele Grüße")
    print("")
    print(f"{absender}")

generate_newsletter(absender)
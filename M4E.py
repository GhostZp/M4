username = str("python")
password = str("rules")

komentou = str(input("Username: "))
komentop = str(input("Password: "))
if komentou == username and komentop == password:
    print("Tervetuloa.")
else:
    komentou = str(input("Username: "))
    komentop = str(input("Password: "))
    if komentou == username and komentop == password:
        print("Tervetuloa.")
    else:
        komentou = str(input("Username: "))
        komentop = str(input("Password: "))
        if komentou == username and komentop == password:
            print("Tervetuloa.")
        else:
            komentou = str(input("Username: "))
            komentop = str(input("Password: "))
            if komentou == username and komentop == password:
                print("Tervetuloa.")
            else:
                komentou = str(input("Username: "))
                komentop = str(input("Password: "))
                if komentou == username and komentop == password:
                    print("Tervetuloa.")
                else:
                    print("Pääsy evätty.")


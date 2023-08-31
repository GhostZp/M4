import random

numero = (random.randint(1,10))
arvaus = int(input("Arvaa numero 1 ja 10 väliltä: "))

while numero != arvaus:
    if arvaus < numero:
        print("Liian pieni.")
        arvaus = int(input("Arvaa uudestaan: "))
    elif arvaus > numero:
        print("Liian iso.")
        arvaus = int(input("Arvaa uudestaan: "))
    else:
        break
print("Onnittelut! Arvasit oikein.")
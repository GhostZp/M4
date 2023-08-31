isoin = None
pienin = None
list = []

while True:
    numerot = input("Kerro numero: ")
    if numerot == "":
        break
    try:
        value = int(numerot)
        list.append(value)
    except ValueError:
        print("Invalid input")
print ("Isoin numero on:" + str(max(list)))
print ("Pienin numero on:" + str(min(list)))
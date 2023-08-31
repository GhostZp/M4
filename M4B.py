komento = int(input("Kerro tuumat: "))
while komento > 0:
    tulos = komento * 2.54
    print(f"{komento} tuumaa on yhtäsuuri kuin {tulos} senttimetriä")
    komento = int(input("Kerro tuumat: "))
    if komento < 0:
      break


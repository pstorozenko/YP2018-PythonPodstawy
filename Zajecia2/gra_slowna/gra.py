odp = input("Czy chcesz wejść do jaskini?")

if odp.lower() == "tak":
    print("To niebezpieczne, musisz być bardzo odważny")
    odp2 = input("Widzisz w oddali czarny, kulisty przedmiot, co to?")
    if odp2.find("bomb") != -1:
        print("TAK, TO BOMBA, <<KABOOM>>")
    else:
        print("Rzeczywiście to", odp2)
    odp3 = input("Napotkany gnom pyta: ,,Jak Ci na imię?''")
    if odp3.endswith("a") and odp3 != 'Kuba':
        odp4 = input("Podróżniczko, co jest czerwone, słodkie i lubi się ze śmietaną?'")
    else:
        odp4 = input("Podróżniku, co jest czerwone, słodkie i lubi się ze śmietaną?'")
    if odp4.lower().find("truskawk") != -1:
        print("Gnom zdradził Ci sekretne hasło")
    else:
        print("Gnom zdenerwowany złym hasłem, rzuca się na Ciebie! UCIEKAJ!!!")
else:
    print("Widzisz w oddali jezioro")


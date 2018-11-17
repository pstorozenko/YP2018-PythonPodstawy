l = [("Piotr", "pizza"), ("Ula", "chińczyk")]

for e in l:
    imie = e[0]
    potrawa = e[1]
    if imie.endswith("a"):
        print("Dzień dobry Pani")
    else:
        print("Dzień dobry Panu")
    print("Życzę smacznego przy jedzeniu", potrawa)

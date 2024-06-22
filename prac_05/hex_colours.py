NAME_TO_HEX = {"Amaranth": "#e52b50",
               "Sunglow": "#ffcc33",
               "Heliotrope": "#df73ff",
               "Lemon": "#fff700",
               "Eminence": "#6c3082",
               "Yellow1": "#ffff00",
               "Wine": "#722f37",
               "Oxblood": "#4a0000",
               "Ochre": "#cc7722",
               "Denim": "#1560bd"}
# Did you notice the first letter of the names of each of the colours I chose, are the letters that spell my name?

print(NAME_TO_HEX)

colour_name = input("Colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} is {NAME_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Colour name: ").title()

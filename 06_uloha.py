def mocniny(seznam, exponent):
    vysledky = []
    for cislo in seznam:
        vysledky.append(cislo ** exponent)
    return vysledky
# Ukazkovy seznam
seznam = [1, 2, 3, 4, 5]
exponent = 2

novy_seznam = mocniny(seznam, exponent)
print("Původní seznam:", seznam)
print("Nový seznam s mocninou", exponent, ":", novy_seznam)

def odstran_cislo(seznam, cislo):
    pocet_odstranenych = seznam.count(cislo)
    for i in range(pocet_odstranenych):
        seznam.remove(cislo)
    return pocet_odstranenych

# Ukazkovy seznam
seznam = [1, 2, 3, 4, 2, 5, 2, 6]
cislo = 2

pocet_odstranenych = odstran_cislo(seznam, cislo)
print("Počet odstraněných prvků:", pocet_odstranenych)
print("Seznam po odstranění čísla", cislo, ":", seznam)

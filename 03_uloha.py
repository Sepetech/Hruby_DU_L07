def pocet_prvocisel(numbers):
    def is_prvocislo(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    for num in numbers:
        if is_prvocislo(num):
            count += 1
    return count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(pocet_prvocisel(numbers))  # Vysledek: 4

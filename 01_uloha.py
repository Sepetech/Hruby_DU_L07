def soucin_prvku(lst):
    result = 1
    for num in lst:
        result *= num
    return result

numbers = [2, 3, 4, 5]
result = soucin_prvku(numbers)
print(result)

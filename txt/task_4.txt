def positive_numbers():
    result = []
    while True:
        number = int(input("Введите число >>> "))
        if number > 0:
            result.append(number)
        else:
            break
    return result

def product_of_numbers(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product
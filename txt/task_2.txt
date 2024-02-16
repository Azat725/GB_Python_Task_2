def commonElementInArrays(array1, array2):
    result = []
    for element in array1:
        if element in array2:
            result.append(element)
    return result

print(commonElementInArrays([1, 2, 3, 4, 5, 6], [1, 2, 3, 7, 8, 9, 1029101201]))
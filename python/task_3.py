words = ['apple', 'banana', 'avocado', 'orange', 'kiwi']
letter = "a" or "A" or "А" or "а"

def start_with_a(array: list, start_letter):
    return [i for i in array if i[0] == start_letter]

print(start_with_a(words, letter))
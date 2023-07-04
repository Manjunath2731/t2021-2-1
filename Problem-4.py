def count(numbers):
    multiples = {num: 0 for num in range(1, 10)}
    for number in numbers:
        for key in multiples.keys():
            if number % key == 0:
                multiples[key] += 1
    return multiples
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = count(numbers)
print("Output:", result)
numbers = [80, 30, 40, 60, 50]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest =", largest)

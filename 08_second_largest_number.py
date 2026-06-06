numbers = [80, 30, 40, 60, 50]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

numbers.remove(largest)

second_largest = numbers[0]

for num in numbers:
    if num > second_largest:
        second_largest = num

print("Second Largest =", second_largest)

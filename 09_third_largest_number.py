numbers = [80, 30, 40, 60, 50]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

temp1 = numbers.copy()
temp1.remove(largest)

second_largest = temp1[0]

for num in temp1:
    if num > second_largest:
        second_largest = num

temp2 = temp1.copy()
temp2.remove(second_largest)

third_largest = temp2[0]

for num in temp2:
    if num > third_largest:
        third_largest = num

print("Third Largest =", third_largest)

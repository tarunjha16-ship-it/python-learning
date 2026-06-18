# While Loop Example

print("=== WHILE LOOP ===")

count = 1

while count <= 5:
    print(count)
    count += 1

print("Loop Finished")


print("\n=== BREAK EXAMPLE ===")

count = 1

while count <= 5:
    if count == 4:
        break

    print(count)
    count += 1


print("\n=== CONTINUE EXAMPLE ===")

count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)

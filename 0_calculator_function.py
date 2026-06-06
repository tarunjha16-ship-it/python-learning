def calc(a, b):

    total = a + b
    diff = a - b
    product = a * b

    if b == 0:
        quotient = "not defined"
        print("Division by zero not allowed")
    else:
        quotient = a / b

    return total, diff, product, quotient


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total, diff, product, quotient = calc(num1, num2)

print("Sum:", total)
print("Difference:", diff)
print("Product:", product)
print("Quotient:", quotient)

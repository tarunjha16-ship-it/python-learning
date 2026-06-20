students = []

file = open("students.csv", "r")

next(file)

for line in file:
    data = line.strip().split(",")

    student = {
        "Name": data[0],
        "Marks": int(data[1]),
        "City": data[2]
    }

    students.append(student)

file.close()

print(students)

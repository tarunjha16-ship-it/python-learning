students=[{"Name": "Mohan", "Marks": 90, "City": "Jaipur"},
{"Name": "Sita", "Marks": 75, "City": "Delhi"},
{"Name": "Geeta", "Marks": 88, "City": "Mumbai"}]

total_marks=0
count=0
for student in students:
    total_marks += student["Marks"]
    count += 1
average_marks = total_marks / count
print("Average marks: ", average_marks)
print("Average marks:", round(average_marks, 2))
print(f"Average marks: {average_marks:.2f}")





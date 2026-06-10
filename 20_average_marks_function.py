def calculate_average_marks(students):
    Total_marks = 0
    for student in students:
        Total_marks += student["Marks"]
        average_marks = Total_marks / len(students)
    return average_marks

average_marks = calculate_average_marks(students)
print("Average marks: ", round(average_marks, 2))

students=[{"Name" : "Mohan", "Marks" : 90, "City" : "Jaipur"},
{"Name" : "Sita", "Marks" : 75, "City" : "Delhi"},
{"Name" : "Geeta", "Marks" : 88, "City" : "Mumbai"}]

def calculate_average_marks(students):
    Total_marks = 0
    for student in students:
        Total_marks += student["Marks"]
    average_marks = Total_marks / len(students)
    return average_marks
    
def find_top_student(students):
    highest_marks = 0
    top_student_name = ""
    for student in students:
        if student["Marks"] > highest_marks:
            highest_marks = student["Marks"]
            top_student_name = student["Name"]
    return top_student_name, highest_marks
average_marks = calculate_average_marks(students)
print("Average marks: ", round(average_marks, 2))
top_student, highest_marks = find_top_student(students)
print("Top student: ", top_student)
print("Highest marks: ", highest_marks)


def find_lowest_student(students):
    lowest_marks= students[0]["Marks"]
    lowest_student=students[0]["Name"]
    for student in students:
        if student["Marks"] < lowest_marks:
            lowest_marks=student["Marks"]
            lowest_student=student["Name"]
    return lowest_student, lowest_marks
lowest_student, lowest_marks = find_lowest_student(students)
print("lowest student :", lowest_student)
print("lowest marks :", lowest_marks)

def find_pass_fail_student(students):
    pass_count=0
    fail_count=0
    for student in students:
        if student["Marks"]>=80:
            pass_count=pass_count+1
        else:
            fail_count=fail_count+1
    return pass_count,fail_count
    
pass_students, fail_students = find_pass_fail_student(students)

print("passed students :", pass_students)
print("fail students :", fail_students)

print("\n===== STUDENT REPORT =====")

print("Top Student:", top_student)
print("Highest Marks:", highest_marks)

print("\nLowest Student:", lowest_student)
print("Lowest Marks:", lowest_marks)

print("\nAverage Marks:", round(average_marks, 2))

print("\nPassed Students:", pass_students)
print("Failed Students:", fail_students)

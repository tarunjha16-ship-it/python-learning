def calculate_average_marks(students):
    total_marks=0
    count=0
    for student in students:
        total_marks += student["Marks"]
        count += 1
    average_marks = total_marks / count
    return average_marks
def find_top_student(students):
    highest_marks=0
    top_student_name=students[0]["Name"]
    for student in students:
        if student["Marks"] > highest_marks:
            highest_marks = student["Marks"]
            top_student_name = student["Name"]
    return top_student_name, highest_marks
def find_lowest_student(students):
    lowest_marks=students[0]["Marks"]
    lowest_student_name=students[0]["Name"]
    for student in students:
        if student["Marks"] < lowest_marks:
            lowest_marks = student["Marks"]
            lowest_student_name = student["Name"]
    return lowest_student_name, lowest_marks
def find_pass_fail_students(students):
    pass_count=0
    fail_count=0
    for student in students:
        if student["Marks"] >= 80:
            pass_count += 1
        else:
            fail_count += 1
    return pass_count, fail_count 


students=[]
file=open("student.csv","r")
next(file)
for line in file:
    data=line.strip().split(",")
    name=data[0]
    marks=int(data[1])
    city=data[2]
    student={"Name": name, "Marks": marks, "City": city}
    students.append(student)
file.close()
print(students)

average_marks = calculate_average_marks(students)
top_student, highest_marks = find_top_student(students)
lowest_student, lowest_marks = find_lowest_student(students)          
pass_students, fail_students = find_pass_fail_students(students)

print("\n===== STUDENT REPORT =====")
print("Top Student:", top_student) 
print("Highest Marks:", highest_marks)
print("\nLowest Student:", lowest_student)
print("Lowest Marks:", lowest_marks)
print("\nAverage Marks:", round(average_marks, 2))
print("\nPassed Students:", pass_students)
print("Failed Students:", fail_students)


===== STUDENT REPORT =====
Top Student: Mohan
Highest Marks: 90

Lowest Student: Sita
Lowest Marks: 75

Average Marks: 84.33

Passed Students: 2
Failed Students: 1

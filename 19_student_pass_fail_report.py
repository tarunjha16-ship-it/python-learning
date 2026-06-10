students=[{"Name": "Mohan", "Marks": 90, "City": "Jaipur"},
{"Name": "Sita", "Marks": 75, "City": "Delhi"},
{"Name": "Geeta", "Marks": 88, "City": "Mumbai"}]

count=0
pass_count=0
fail_count=0
for student in students:
    count += 1

    if student["Marks"] >= 80:
        pass_count += 1
    else:
        fail_count += 1


print("Total students: ", count)
print("Passed students: ", pass_count)  
print("Failed students: ", fail_count)


students=[{"Name" : "Mohan", "Marks" : 90}, {"Name" : "Sita", "Marks" : 75}, {"Name" : "Geeta", "Marks" : 88}, ]
def find_lowest_student(students):
    lowest_marks= students[0]["Marks"]
    lowest_student=students[0]["Name"]
    for student in students:
        if student["Marks"] < lowest_marks:
            lowest_marks=student["Marks"]
            lowest_student=student["Name"]
    return lowest_marks, lowest_student

lowest_marks, lowest_student = find_lowest_student(students)


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





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




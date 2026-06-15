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



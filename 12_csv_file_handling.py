with open("student.csv","w") as file:
    file.write("Name, Marks\n")
    file.write("Ram,80\n")
    file.write("Mohan,90\n")
    file.write("Sita,75\n")
    file.write("Geeta,88\n")
file.close()
file=open("student.csv","r")
content=file.read()
print(content)
file.close()

file = open("student.csv", "r")

for line in file:
    print(line)

file.close()

file=open("student.csv", "r")
next(file )
highest_marks=0
top_student=""
total_marks=0
count=0
for line in file:
    
    data=line.strip().split(",")
    name=data[0]
    marks=int(data[1])
    total_marks += marks
    count += 1
    avarage_marks = total_marks / count
    
    if marks > highest_marks:
        highest_marks=marks
        top_student=name
    print(name, "scored", marks)
file.close()

print("Top student: ", top_student)
print("Highest marks: ", highest_marks)
print("Average marks: ", avarage_marks)


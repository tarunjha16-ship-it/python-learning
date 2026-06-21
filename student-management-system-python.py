students=[] #students list
file=open("students.csv","r")
next(file)
for line in file:
    data=line.strip().split(",") #split() ek string ko todkar list bana deta hai.
        # student dictionary
    if len(data) < 3:
        continue
    student={
            "Name" : data[0],
            "Marks" : int(data[1]),
            "City" : data[2]
            }
    students.append(student) #students list me student dictionary will append
file.close()
#print(students)
def show_students(students):
    for student in students:
        print(student["Name"], "-", student["Marks"], "-", student["City"] )
   

def search_student(students):
    search_name=input("Enter student name to search : ")
    found = False
    for student in students:
        if student["Name"].lower()==search_name.lower():
            print("Student Found : ")
            print(student)
            found=True
            break
    if not found:
        print("Student Not found")
#def close_program():

def add_student(students):
    name=input("Enter Student Name : ")
    for student in students:
        if student["Name"].lower() == name.lower():
            print("Student already exists")
            return
    marks=int(input("Enter Student Marks : "))
    city=input("Enter Student City : ")
    new_student={"Name" : name, "Marks" : marks, "City" : city}
    file=open("students.csv","a")
    students.append(new_student)
    file.write("\n"+ name + "," +str(marks)+ "," + city)
    file.close()
    print("Student Added Successfully....")

def delete_student(students):
    delete_student_name = input("Enter Student name to delete : ")
    found = False
    
    
    for student in students:
        if student["Name"].lower() == delete_student_name.lower():
            input_yes_no=input("Are you sure you want to delete : "+ delete_student_name+ " Type Yes/No\n")
            if input_yes_no.lower()=="yes":
                students.remove(student)
                print("Student Deleted Successfully..")
                found = True
                break
            elif input_yes_no.lower()=="no":
                return

    if not found:
        print("student not found")

def update_student(students):
    found=False
    search_student=input("Enter Student Name to update : ")
    for student in students:
        if student["Name"].lower()==search_student.lower():
            print("Student found")
            found=True
            new_marks=int(input("Enter student Marks : "))

            student["Marks"]=new_marks
            print("Student Marks Updated Successfully...")
            break
    if not found:
        print("Student not found")

    
def save_students_to_csv(students):
    file=open("students.csv","w")
    file.write("Name,Marks,City\n")
    for student in students:
        file.write(student["Name"]+","+ str(student["Marks"])+","+student["City"]+"\n")
    file.close()

while True:
    

    print("====Student Report System=====\n")
    print("Menu to Enter Choice\n")
    print("1. Show Student\n")
    print("2. Search Student\n")
    print("3. Add Student\n")
    print("4. Delete Student\n")
    print("5. Update Student\n")
    print("6. Exit\n")
    choice=input("Enter a choice : ")
    if choice=="1":
        show_students(students)
    elif choice=="2":
        search_student(students)
    elif choice=="3":
        add_student(students)
    elif choice=="4":
        delete_student(students)
        save_students_to_csv(students)
    elif choice=="5":
        update_student(students)
        save_students_to_csv(students)
    elif choice=="6":
        print("program closed")
        break
    else:
        print("Invalid Choice")
    
    


            



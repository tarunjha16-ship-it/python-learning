students=[{"Name" : "Mohan", "Marks" : 90, "City" : "Jaipur"},
{"Name" : "Sita", "Marks" : 75, "City" : "Delhi"},
{"Name" : "Geeta", "Marks" : 88, "City" : "Mumbai"}]

while True:
    print("\n===MENU===")   
    print("\n 1. Show Students")
    print("\n 2. Search Students")
    print("\n 3. Add Students")
    print("\n 4. Exit")
    
    choice = input("Enter your choice (1-4): ")
   
    if choice == "1":
       
        for student in students:
            print(student["Name"], "-" , student["Marks"], "-", student["City"])
    elif choice=="2":
        search_name=input("Enter student name : ")
        found=False
        for student in students:
            if(student["Name"].lower()==search_name.lower()):
                print("Student Found")
                print(student)
                found=True
                break
        if not found:
            print("Student not found")
    elif choice == "3":
        print("Enter student details to add")
        Name=input("enter name:")
        Marks=int(input("Enter Marks :"))
        City=input("Enter City :")
        new_student={"Name" : Name, "Marks" : Marks, "City" : City}
        students.append(new_student)
        print("Student Added Successfully")
    elif choice == "4":
        print("Program Closed.")
        break








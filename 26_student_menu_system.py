students=[{"Name" : "Mohan", "Marks" : 90, "City" : "Jaipur"},
{"Name" : "Ram", "Marks" : 75, "City" : "Delhi"},
{"Name" : "Geeta", "Marks" : 88, "City" : "Mumbai"}]

while True:
    print("\n===MENU===")   
    print("\n 1. Show Students")
    print("\n 2. Search Students")
    print("\n 3. Exit")
    
    choice = input("Enter your choice (1-3): ")
   
    if choice == "1":
       
        for student in students:
            print(student["Name"], "-" , student["Marks"] )
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
        print("Program Closed.")
        break



    






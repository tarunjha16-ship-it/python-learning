name = input("Enter Name: ")
marks = input("Enter Marks: ")
city = input("Enter City: ")

file = open("students.csv", "a")

file.write("\n" + name + "," + marks + "," + city)

file.close()

print("Student Saved Successfully")

students.csv
Name,Marks,City
Mohan,90,Jaipur
Sita,75,Delhi
Geeta,88,Mumbai




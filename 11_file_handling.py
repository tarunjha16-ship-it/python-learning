with open("my_profile.txt", "w") as file:
    file.write("Name: Study Mitra\n")
    file.write("Education: MCA\n")
    file.write("Profession: Government Employee\n")
    file.write("Python Day: 6\n")

with open("my_profile.txt", "r") as file:
    content = file.read()
    print(content)

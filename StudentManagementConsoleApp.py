
students = []

while True:
    print("<---Student Management Console App--->")
    print("A. Add Student")
    print("B. View All Students")
    print("C. Search Student")
    print("D. Update Marks")
    print("E. Exit")

    choice = input("Enter your choice: ")

    if choice == 'A':
        student = {}

        student["name"] = input("Enter your name: ")
        student["age"] = int(input("Enter your age: "))
        student["marks"] = int(input("Enter your marks: "))
        
        students.append(student)
        print(f"Student: {student}")
        print("Student successfully added!")

    elif choice  == "B":
        if students:
            for student in students:
                print("Student:", student)
        else:
            print("Student not found!")
    elif choice == "C":
        name = input("Enter a name to search: ")

        for student in students:
            if student["name"] == name:
                print(student)
                break
    elif choice == "D":
        name = input("Enter a name of the student: ")
        new_marks = int(input("Enter new marks: "))

        for student in students:
            if student["name"] == name:
                student["marks"] = new_marks
                print("New marks: ", new_marks)
                break
    elif choice == "E":
        print("Byeeee...")
        break
    else:
        print("Invalid!")
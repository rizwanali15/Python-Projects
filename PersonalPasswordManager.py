
import random
import string

password = {}

try:
    with open("password.txt") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            password[website] = pwd
except:
    pass

def generate_password():
    char = string.ascii_letters + string.digits + "@._#%/!"
    password = "".join(random.choice(char) for _ in range(8))
    return password

while True:
    print("---Personal Password Manager---")
    print('1. Save Password')
    print('2. View Passwords')
    print('3. Generate Password')
    print('4. Exit')

    choice = input("Enter your choice: ")

    if choice == "1":
        website = input("Enter website: ")
        pwd = input("Enter your password: ")
        password[website] = pwd

        with open("password.txt", "a") as file:
            file.write(f"{website} : {pwd}")

        print("Saved!")
    elif choice == "2":
        if not password:
            print("Not found!")
        else:
            for website, pwd in password.items():
                print(website, ":", pwd)

    elif choice == "3":
        print("Generated Password: ", generate_password())
    elif choice == "4":
        print("Babyeeeee....")
        break
    else:
        print("Invalid!")
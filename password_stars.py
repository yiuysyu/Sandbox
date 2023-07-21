MIN_LENGTH = 8

while True:
    password = input("Enter your password: ")

    if len(password) < MIN_LENGTH:
        print(f"The password doesn't meet a minimum length {MIN_LENGTH} characters long. Please enter again.")
    else:
        print("*" * len(password))
        break

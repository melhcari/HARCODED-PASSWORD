password = "admin123"

def login():
    user = input("Enter password: ")
    if user == password:
        print("Access granted")

login()

while True:
    name = input("your name: ");
    password = input("your password: ");

    if name == password:
        print("same answers, it's incorrect!")
    else:
        break;

print(f"{name} and password {password} registered");
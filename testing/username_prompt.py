def username_prompt():
    while True:
        name = input("Please enter your name: ")
        if not name:
            print("Every sailor has a name? Try again!")
        elif name.isnumeric():
            print("Every sailor has a name? Not a number!")
        else:
            break
    return name


sailors_name = username_prompt()
print(f"\nWelcome aboard Sailor {sailors_name.upper()}! Ready to sink some ships!")

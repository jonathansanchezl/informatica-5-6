def main():
    validated = True
    while validated:
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if number >= 1 and number <= 10:
                print("Success! ")
                validated = False
            else:
                print("Between 1 AND 10! ")
        except ValueError:
            print("You must enter a NUMBER: ")

    nmb = True
    while nmb:
        try:
            name = input("Enter your name: ")
            if name == "":
                print("You must enter your name!!!: ")
            else:
                print(f"Stored name: {name}")
                nmb = False
        except ValueError:
                print("You MUST enter your name!!! ")
if __name__ == "__main__":
    main()

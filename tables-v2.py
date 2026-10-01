def main():
    print("Welcome to the times table quiz")
    first = True
    while first:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on: "))
            first = False
        except ValueError:
            print("Invalid")
    second = True
    while second:
        try:
            max_value = int(input("enter maximum value for the times table: "))
            second = False
        except ValueError:
            print("Invalid")

    print(f"Here is your quiz on the {times_table} times table")
    value = 3
    for x in range(1,max_value + 1):
        answer = x * int(times_table)
        third = True
        while third:
            try:
                user_answer = int(input(f"{x} times {times_table} is: "))
                third = False
            except ValueError:
                 print("invalid")
        if user_answer == answer:
            print("Correct")
        else:
            print("incorrect")
            value -= 1
        if value == 0:
             break

    if value <= 0:
            print("You failed")
    else:
            print("Good job")


if __name__ == "__main__":
    main()

def main():
    while True:
        number = int(input("Enter a number (1-10): "))
        if number <= 10:
             if number > 0:
                numbers = [1,2,3,4,5,6,7,8,9,10]
                for i in numbers:
                    number2 = number*i
                    print(f"1 times {number} is {number2}")
        exit = input("Do you want another or exit? ").strip().lower()
        if exit == "another":
            print("")
        elif exit == "exit":
            break
        else:
            print("type what you want to do between another or exit")

if __name__ == "__main__":
    main()

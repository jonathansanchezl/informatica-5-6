def main():
    while True:
        number = int(input("Enter a number (1-10): "))
        numbers = [1,2,3,4,5,6,7,8,9,10]
        for i in numbers:
             number2 = number*i
             print(f"1 times {number} is {number2}")
        if number <=10:
                if number > 0:


if __name__ == "__main__":
    main()

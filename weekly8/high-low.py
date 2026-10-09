def main():
    def highest(a,b):
        if a > b:
            highest_num = a
        else:
            highest_num = b
        print(f"Highest numb: {highest_num}")

    numb1 = int(input("enter first number: "))
    numb2 = int(input("enter second number: "))
    highest(numb1,numb2)




    def lowest(a,b,c):
        if a > b:
            lowest_num = b
        elif a < b:
            lowest_num = a
        else:
            lowest_num = c
        print(f"lowest numb: {lowest_num}")

    numb1 = int(input("enter first number: "))
    numb2 = int(input("enter second number: "))
    numb3 = int(input("enter third number: "))
    lowest(numb1,numb2,numb3)


if __name__ == "__main__":
    main()

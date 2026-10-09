def main():
    print("Binary to Decimal Converter")
    print("This program will convert any binary number into a decimal number")
    binary = []
    binary2 = []
    elevates = []

    def binary_to_decimal(a):
        binary.append(a)
        for i in str(binary):
            lis = int(i)
            binary2.append(lis)
        for i2 in binary2:
            numbers = 0
            numbers += 1
        for i3 in binary2:
            elevate = i3 ** numbers
            elevates.append(elevate)
            numbers -=1
        for i4 in elevates:
            final = i4 + i4
        final2 = final/2

        print(f"Your number is {final2}")

    try:
        decimal = int(input("Enter a number "))
    except ValueError:
        print("Invalid")

    binary_to_decimal(decimal)


if __name__ == "__main__":
    main()

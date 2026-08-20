def main():

    transistors = float(input("Enter the number of transistors(billions): "))
    years = int(input("Enter the number of years: "))
    y2 = years/2
    y3 = 2**y2

    final = transistors*y3


    print(f"Transistors in future(billions): {final}" )

if __name__ == "__main__":
     main()

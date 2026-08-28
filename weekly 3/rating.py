def main():
    print("superwings")
    rateing = float(input("enter a decimal number from 0 to 5 to rate The restaurant: "))

    if rateing < 5:


    if rateing > 4.5:
         print("perfection")
    elif rateing > 4:
         print("Excellent")
    elif rateing > 3:
             print("Good")
    elif rateing > 2:
             print("Fair")
    elif rateing < 2:
             print("Poor")

    else:
         print("invalid value")
if __name__ == "__main__":
     main()

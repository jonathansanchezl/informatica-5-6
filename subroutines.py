def main():
     def calculate(a,b):
          answer = a+b
          print(f"{a}+{b}={answer}")
     numb1 = 10
     numb2 = 15

     calculate(numb1, numb2)

     def average_value(a, b, c):
          answer =(a+b+c) / 3
          print(f"The average value is {round(answer, 1)}")
     numb3 = float(input("enter first number: "))
     numb4 = float(input("enter second number: "))
     numb5 = float(input("enter third number: "))

     average_value(numb3, numb4, numb5)



if __name__ == "__main__":
    main()

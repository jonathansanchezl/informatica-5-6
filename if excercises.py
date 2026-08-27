def main():
    inte = int(input("enter an integer numer: "))
    if inte < 0:
         print(inte*-1)
    else:
         print(inte)

    inte2 = float(input("enter a numer: "))
    inte3 = float(input("enter a numer: "))
    math = input("enter a math sign: ")
    if math == "+":
         print(inte2+inte3)
    elif math == "-":
         print(inte2-inte3)
    elif math == "*":
         print(inte2*inte3)
    else:
         print("nothing")



    func = input("write an aritmethic operation: ")
    parts = func.split(" ")
    numb1 = float(parts[0])
    op = parts[1]
    numb2 = float(parts[2])

     if op == "+":
             print(numb2+numb1)
     elif op == "-":
             print(numb1-numb2)
     elif op == "*":
             print(numb1*numb2)
     else:
             print("nothing")




if __name__ == "__main__":
     main()

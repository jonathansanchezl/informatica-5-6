def main():
    layer = input("Descnet atmosphere layer: ")
    if layer == "Exosphere":
            print("your altitude level will be between 700-10,000km")
    elif layer == "Thermosphere":
             print("your altitude level will be between 85- 700km")
    elif layer == "Mesosphere":
             print("your altitude level will be between 50-85km")
    elif layer == "Stratosphere":
             print("your altitude level will be between 12-50km")
    elif layer == "Troposphere":
             print("your altitude level will be between 0-12km")
    else:
             print("insert a valid atmosphere layer")
    exact = int(input("Enter exact altitude: "))
    ex = 2000
    Th = 500
    Me = 200
    st = 75
    tr = 20
    if exact > 699:
            m = exact-700
            e = (m*1000)/ex
            e1 = 615000/Th
            e2 = 35000/Me
            e3 = 38000/st
            e4 = 12000/tr
            e5 = round(e+e1+e2+e3+e4, 2)
            print(e5, "seconds")
    elif exact > 84:
            m2 = exact-85
            a = (m2*1000)/Th
            a2 = 35000/Me
            a3 = 38000/st
            a4 = 12000/tr
            a5 = round(a+a2+a3+a4, 2)
            print(a5, "seconds")
    elif exact > 49:
            m3 = exact-50
            b = (m3*1000)/Me
            b3 = 38000/st
            b4 = 12000/tr
            b5 = round(b+b3+b4, 2)
            print(b5, "seconds")
    elif exact > 11:
            m4 = exact-12
            c = (m4*1000)/st
            c4 = 12000/tr
            c5 = round(c+c4, 2)
            print(c5, "seconds")
    elif exact > 0:
            d = (exact*1000)/tr
            d2 = round(d, 2)

            print(d2, "seconds")
    else:
            print("enter a valid value")


if __name__ == "__main__":
     main()

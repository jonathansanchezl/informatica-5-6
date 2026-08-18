def main():

    colombia = float(input("amount of colombian pesos: "))
    peru = float(input("amount of Peruvian soles: "))
    brazil = float(input("amount of Brazilian reais: "))

    mxcol = colombia*0.0054
    uscol = colombia*0.00032

    mxper = peru*5.07
    usper = peru*0.30

    mxbra = brazil*3.27
    usbra = brazil*0.19

    totalmx = mxcol + mxper + mxbra
    totalus = uscol + usper + usbra

    mxred = round(totalmx, 2)
    usred = round(totalus, 2)

    print(f"USD: {usred}" )
    print(f"MX: {mxred}" )




if __name__ == "__main__":
     main()

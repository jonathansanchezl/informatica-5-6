def main():

    def welcome():
        menu = ["Cheeseburguer","Fries","Soda","Ice cream","Cookie"]
        print("Welcome to Wendys!")
        print("Here is the menu: ")
        value = 1
        for i in menu:
            print(f"{value}. {i}")
            value += 1
    welcome()

    def get_item(a):
        if a == 1:
            print("Your order is Cheeseburguer🍔")
        elif a == 2:
            print("Your order is Fries🍟")
        elif a == 3:
            print("Your order is Soda🥤")
        elif a == 4:
            print("Your order is Ice cream🍦")
        elif a == 5:
            print("Your order is Cookie🍪")
        else:
            print("Select something from the menu")

    try:
        order = int(input("What would you like to order?(select your order useing the number 1-5) "))
    except ValueError:
        print("Invalid")

    get_item(order)


if __name__ == "__main__":
    main()

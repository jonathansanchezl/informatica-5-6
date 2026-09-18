def main():
    list = []
    while True:
            first = input("Do you have anything to do? " ).strip().lower()
            if first == "yes":
                add = input("do we have to add of delete anything? " ).strip().lower()
            else:
                print("enjoy your free time!")
                break
            if add == "yes":
                add = input("Do we need to add something? ").strip().lower()
                if add == "yes":
                    tasks = input("what do we add? " )
                    list.append(tasks)
                    print(f"we need to do:", list)
                elif add == "no":
                    dele = input("do we need to delete something? ")
                    if dele == "yes":
                        print(list)
                        delete = input("what do we delete? ")
                        list.remove(delete)
    print(list)


if __name__ == "__main__":
    main()

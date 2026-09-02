def main():
    answer = ""
    while answer != "yes!":
        answer = input("Are we there yet? ").strip().lower()
        print("we are here")
        if answer == "yes":
            followup = input("really? ").strip().lower()
        if followup == "Yes":
            break
if __name__ == "__main__":
    main()

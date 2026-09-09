import random
def main():
    options = ["heads", "tails"]
    attempts = 3
    while attempts > 0:
        value = random.choice(options)
        guess = input("heads or tails?: ").strip().lower()
        print("the coin landed on", value)
        if guess == value:
            print("winner")
            break
        else:
            print("looser")
            attempts -=1
            print("attempts left:", attempts)
if __name__ == "__main__":
    main()

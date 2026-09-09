import random
def main():
    name = input("Hello! What is your name? ").strip().lower()
    dif = input("What difficult do you want, easy, medium or hard? ").strip().lower()
    if dif == "easy":
        answer = random.randint(1, 20)
        num1 = "1"
        num2 = "20"
    elif dif == "medium":
        answer = random.randint(1, 100)
        num1 = "1"
        num2 = "100"
    elif dif == "hard":
        answer = random.randint(1, 1000)
        num1 = "1"
        num2 = "1000"
    else:
        print("enter a valid value")

    attempts = 10
    while attempts > 0:
        guess = int(input(f"Well, {name} I am thinking of a number between {num1} and {num2}, Take a guess "))
        if guess < answer:
            print("your guess is too low")
            attempts -= 1
        elif guess > answer:
            print("your guess is too high")
            attempts -= 1
        elif guess == answer:
            print(f"Good job, {name}! You guessed my number!")
            break
        else:
            print("enter a valid value")
if __name__ == "__main__":
    main()

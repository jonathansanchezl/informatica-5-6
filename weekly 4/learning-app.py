import random
def main():
    print("Math app!")
    streak = 0
    while streak < 3:
        math1 = random.randint(1, 99)
        math2 = random.randint(1, 99)
        operation = int(input(f"What is {math1} + {math2}? "))
        print(f"your answer: {operation}")
        math3 = math1 + math2
        if operation == math3:
            streak += 1
            streak2 = "⭐"*streak
            print("Correct!")
            print(f"streak:{streak2}")
        else:
            streak = 0
            print("incorrect")
            print(f"the answer was {math3}")
if __name__ == "__main__":
    main()

import random
guess = int(input("heads or tails: "))
value = random.randint(1, 2)
if value == 1:
    print("heads")
elif value == 2:
    print("tails")
else:
    print("enter a valid value")
if guess == value:
    print("You win!")
else:
    print("You lose :c")


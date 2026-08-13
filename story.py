def main():
#  planet = input("planet:")
#  #separation
#  print("Hello", planet)
#  #concatenation
#  print("hello " + planet)
# #formatted strings
#  print(f"hello {planet}")
# #ending
#  print("hello", end=" ")
 #  print(planet)

    name = input("what is your name? ").strip().title()
    color = input("name a color: ").strip().lower()
    adjetive = input("Give me an adjetive: ").strip().lower()
    goal = input("A goal you would like to achieve: ").strip().lower()

    print("Hello,", name)

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adjetive}. I decided today I will finally {goal}.")


    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adjetive}. I decided today I will finally {goal}.")

    yell=(f"At dawn the sky turned {color}, and the air felt {adjetive}. I decided today I will finally {goal}.")
    print(yell.upper())


if __name__ == "__main__":
 main()


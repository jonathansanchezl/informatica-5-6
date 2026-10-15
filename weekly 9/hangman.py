#define main()
#   print(welcome)
#   pull random words from a list
#   ask for a letter
#   if the word has that letter, search for the same letter but in other position in the word, reveal all the positions for that letter
#   if the word hasnt that letter, substract 1 opportunitie from the 5 opportunities
#   keep asking until the word is complete or the opportunities are gone
#
#
import random
def main():
    def start_game():
        #tun file into a list
        wordslist = []
        with open ("words.txt") as words:
            for line in words:
                line = line.replace("\n","")
                wordslist.append(line)
            word_selected = random.choice(wordslist)
            print(word_selected)
            letters = list(word_selected)
            print("_ "* len(letters))
            while True:
                guess = input("Guess a letter: ")
                for i in letters:
                    if i == guess:
                        print("correct")


    start_game()


if __name__ == "__main__":
    main()

### Importing Modules
import random
from lists_for_hangman import Five_letter_words, Six_letter_words, Eight_letter_words, Hangman
replay = "Y"

replay_options = ["Y", "y", "N", "n"]
diff_options = ["B", "b", "I", "i", "A", "a"]
###

while replay == "Y" or replay == "y":

    ### Declaring Variables
    strikes = 7
    already_guessed = ""
    ###

    ### Pre-Game
    print("Welcome to Hangman!")
    Rules = input("Do you already know how to play?\n[Y] Yes\t[N] No\n")
    while Rules not in replay_options:
        print("Invalid input!")
        Rules = input("Do you already know how to play?\n[Y] Yes\t[N] No\n")
    if Rules == "N" or Rules == "n":
        print("No worries!\nAll you have to do is guess the word one letter at a time.\nEverytime you guess a wrong letter, your 'man' gets closer to getting hanged.\nEverytime you guess correctly... The letter is placed into the correct place.\nThat's about it! Best of luck!")
    Difficulty = input("Please choose a Difficulty:\n[B] Begginer\t[I] Intermediate\t[A] Advanced\n")
    while Difficulty not in diff_options:
        print("Invalid input")
        Difficulty = input("Please choose a Difficulty:\n[B] Begginer\t[I] Intermediate\t[A] Advanced\n")
    if Difficulty == "B" or Difficulty == "b":
        Word = random.choice(Five_letter_words)
    elif Difficulty == "I" or Difficulty == "i":
        Word = random.choice(Six_letter_words)
    elif Difficulty == "A" or Difficulty == "a":
        Word = random.choice(Eight_letter_words)
    Word = Word.upper()
    ###

    ### Game Beginning
    print("You have 7 turns left!")
    print(Hangman[0])
    ###

    ### Main Gameloop
    while (strikes>0):
        Failed = False
        word_print = ""
        for letter in Word:
            if letter in already_guessed:
                word_print+=letter
                word_print+=" "
            else:
                word_print+="_ "
                Failed = True
        print(word_print)
        if (Failed == False):
            print("You Win!!! The word was:", Word)
            break
        guess = input ("Enter a character:\n")
        if (guess=="/cheat"):
            print("Cheat code activated.")
            print("The word is:", Word)
        else:
            guess = guess.upper()
            if (len(guess)==1):
                if guess in already_guessed:
                    print("This letter has already been guessed!")
                elif (guess not in Word):
                    strikes-=1
                    print("Wrong Guess!\t\t\t\tYou have", strikes, "turns left!")
                else:
                    print("Correct guess!\t\t\t\tYou have", strikes, "turns left!")
                print(Hangman[-strikes-1])
                already_guessed+=guess
            else:
                print("Invalid input!")
    ###

    ### Game End Check
    if (Failed==True):
        print("You Lose!!! The word was:", Word)
    replay = input("Would you like to play again?\n[Y] Yes\t[N] No\n")
    while (replay not in replay_options):
        print("Invalid input!")
        replay=input("Would you like to play again?\n[Y] Yes\t[N] No\n")
if replay == "N" or replay == "n":
    print("Thank you for playing Hangman!")
    input("Press enter to continue...")
    ###

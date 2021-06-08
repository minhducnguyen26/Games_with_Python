# Import a list from an external file
from words import word_list

import random

# Get a random word from word_list and return the word uppercased
def get_word():
    word = random.choice(word_list)
    return word.upper()

# The gameplay
def play(word):
    
    # Set variables and lists
    word_completion = "_" * len(word) # Display the "_" == the length of the random word for the player to guess
    guessed = False                   # The variable "guessed" is initially false
    guessd_letters = []               # Empty list
    guessed_words = []                # Empty list
    tries = 6                         # The number of tries until the hangman is completely drawed

    # This is how the game looks like for each time the player guess a letter or a word
    print("Let's play Hangman!")      # Start the game
    print(display_hangman(tries))     # Display the image (the first stage) in the game (the function down below)
    print(word_completion)            # Display the "_" for the player to guess
    print("\n")                       # New line

    # Set conditions for the gameplay
    # While the player hasn't guessed anything and his tries > 0 (the hangman is not completely drawed)
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()    # This line asks the player to guess a letter or a word
        
        # If the player guesses a letter and the guess is a letter in the alphabet
        if len(guess) == 1 and guess.isalpha():
            # If the player repeats his previous guess
            if guess in guessd_letters:                             # The letter is already in the guess_letters list
                print("You already guessed the letter", guess)
            # If the player's guess is wrong
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1                                          # Reduce one try and the main image of the game will draw a line 
                guessd_letters.append(guess)                        # Add the letter in the guess_letters list
            # If the player guesses the correct letter
            else:
                print(guess, "is in the word!")                     
                guessd_letters.append(guess)                        # Add the letter in the guess_letters list
                word_as_list = list(word_completion)                # Convert word_completion from a string of "_" to a list
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess                     # Replace each of the "_" with the letter which the player guesses
                word_completion = "".join(word_as_list)             # Convert word_completion back to a string
                # There is a possibility that the letter which the player guesses completes the word
                # If all of the "_" are replaced by letters
                if "_" not in word_completion:
                    guessed = True                                  # Meaning the player guesses the letter(s)/word correctly
        
        # If the player guess a word and the each letter in the guessed word is in the alphabet
        elif len(guess) == len(word) and guess.isalpha():
            # If the player repeats his previous guess
            if guess in guessed_words:
                print("You already guessed the word", guess)
            # If the player's guess is not the word
            elif guess != word:
                print(guess, "is not in the word.")
                tries -= 1
                guessd_letters.append(guess)
            # If the player guesses the correct word
            else:
                guessed = True                                      # Meaning the player guesses the word correctly
                word_completion = word                              # Change the "_" to the correct completed word

        # If the player doesn't guess any letter or word
        else:
            print("Not a valid guess.")

        print(display_hangman(tries))                               # Display the next stage of the game (the function down below)
        print(word_completion)                                      # Display the "_" for the player to continue his game
        print("\n")                                                 # Newline

    # If "guessed" = True (meaning the player successfully guesses all the letters or the word)
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

# The main image displays each stage in the game (7 stages from the beginning until the hangman is completely drawed)
def display_hangman(tries):
    stages = [  """
                    --------
                    |       |
                    |       o
                    |      \\|/
                    |       |
                    |      / \\
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |      \\|/
                    |       |
                    |      / 
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |      \\|/
                    |       |
                    |      
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |      \\|
                    |       |
                    |      
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |       |
                    |       |
                    |      
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |       
                    |       
                    |      
                    -
                """,
                """
                    --------
                    |       |
                    |       
                    |       
                    |       
                    |      
                    -
                """
    ]
    # Each stage == each try
    return stages[tries]

# The main function shows how the game works and the two functions follow each other in order
def main():
    word = get_word()
    play(word)
    
    # The option to replay/quit the game
    while input("\n \nPlay Again? (Y/N) ").upper() == "Y":
        print("\n")
        word = get_word()
        play(word)
    else:
        input('Thank you for playing! Press "Enter" to quit. ')

# This condition is to run the main function
if __name__ == "__main__":
    main()
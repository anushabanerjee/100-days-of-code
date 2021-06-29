import random
#Importing the two modules for art and word
import hangman_art, hangman_words

# PLEASE NOTE: The following code was written in Replit. Please run it on Replit to get the best experience.
from replit import clear
#Printing the logo
print(hangman_art.logo)

#Choosing a random word from the word list
level = input("Choose Level: Easy or Hard\n")
if level.lower() == "easy":
    chosen_word = random.choice(hangman_words.word_list_easy)
elif level.lower() == "hard":
    chosen_word = random.choice(hangman_words.word_list_hard)
else:
    print("You entered something other than \"easy\" and \"hard\". A random word has been chosen.")
    chosen_word = random.choice(hangman_words.word_list_hard)
word_length = len(chosen_word)

#Initialising the game-enders
end_of_game = False
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks in the displayed list
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Clearing the screen for better UI
    clear() #IMPORTANT: REPLIT ONLY.


    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word let them know it's not in the word.
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Game over.")
            print(f"The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #print the art
    print(hangman_art.stages[lives])
    
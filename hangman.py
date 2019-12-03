# Problem Set 2, hangman.py
# Name: Bondar Illya, KM - 93
# Collaborators: ---
# Time spent: ---

# Hangman Game
# ----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)

# -----------------------------------
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if not i in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    result = ""
    for i in secret_word:
        if not i in letters_guessed:
            result += " _ "
        else:
            result += i
    return result


def get_available_letters(letters_guessed):
    all = string.ascii_lowercase
    result = ""
    for i in all:
        if not i in letters_guessed:
            result += i
    return result


def hangman(secret_word):
    all = string.ascii_lowercase
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " ,len(secret_word), " letters long.")
    warnings_left = 3
    guesses_left = 6
    print("You have " + str(warnings_left) + " warnings left")
    vowel = "aeio"
    letters_guessed = ""
    while not guesses_left == 0:
        print("-------------")
        print("You have " + str(guesses_left) + " guesses left")
        print("Available letters: ",get_available_letters(letters_guessed))
        letters_guessed_input = input("Please guess a letter: ").lower()
        if len(letters_guessed_input) > 1 or len(letters_guessed_input) == 0:
            warnings_left -= 1
            if warnings_left >= 0:
                print("Oops! That is not a valid letter. You have " + str(warnings_left) + " warnings left: "
                      ,get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: "
                      ,get_guessed_word(secret_word, letters_guessed))
                continue
        elif not letters_guessed_input in all:
            warnings_left -= 1
            if warnings_left >=0:
                print("Oops! That is not a valid letter. You have " + str(warnings_left) + " warnings left: "
                      , get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no  warnings left so you lose one guess: "
                      , get_guessed_word(secret_word, letters_guessed))
                continue
        elif letters_guessed_input in letters_guessed:
            warnings_left -= 1
            if warnings_left >=0 :
                print("Oops! You've already guessed that letter. You have " + str(warnings_left) + " warnings left: "
                      , get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "
                      , get_guessed_word(secret_word, letters_guessed))
                continue
        elif letters_guessed_input in secret_word:
            letters_guessed += letters_guessed_input
            if is_word_guessed(secret_word, letters_guessed) == True:
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                print("-------------")
                print("Congratulations, you won!")
                print("Your total score for this game is: ", len(set(secret_word)) * guesses_left)
                break
            else:
                print("Good guess: ",get_guessed_word(secret_word, letters_guessed))
                continue
        elif not letters_guessed_input in secret_word:
            letters_guessed += letters_guessed_input
            if letters_guessed_input in vowel:
                guesses_left -=2
                print("Oops! That letter is not in my word: ",get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_left -=1
                print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
    if guesses_left <=0:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was " + secret_word)
# -----------------------------------
def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i in range(0, len(my_word)):
        if my_word[i] == "_":
            continue
        if my_word[i] != other_word[i]:
            return False
    return True



def show_possible_matches(my_word):
    res = ""
    for word in wordlist:
        if match_with_gaps(my_word,word) == True:
            res +=  " "+word+" "
        else:
            continue
    print(res)


def hangman_with_hints(secret_word):
    all = string.ascii_lowercase
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " ,len(secret_word), " letters long.")
    warnings_left = 3
    guesses_left = 6
    print("You have " + str(warnings_left) + " warnings left")
    vowel = "aeio"
    letters_guessed = ""
    while not guesses_left == 0:
        print("-------------")
        print("You have " + str(guesses_left) + " guesses left")
        print("Available letters: ",get_available_letters(letters_guessed))
        letters_guessed_input = input("Please guess a letter: ").lower()
        if letters_guessed_input == "*":
            letters_guessed += letters_guessed_input
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            while "*" in letters_guessed:
                letters_guessed_input = input("Please guess a letter: ").lower()
                if len(letters_guessed_input) > 1 or len(letters_guessed_input) == 0:
                    print("Oops! That is not a valid letter: ",get_guessed_word(secret_word, letters_guessed))
                    continue
                if not letters_guessed_input in all:
                    print("Oops! That is not a valid letter:",get_guessed_word(secret_word, letters_guessed))
                    continue
                if letters_guessed_input in letters_guessed:
                    print("Oops! You've already guessed that letter: ",get_guessed_word(secret_word, letters_guessed))
                    continue
                if letters_guessed_input in secret_word:
                    letters_guessed += letters_guessed_input
                    if is_word_guessed(secret_word, letters_guessed) == True:
                        print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                        print("-------------")
                        print("Congratulations, you won!")
                        print("Your total score for this game is: 0 ")
                        break
                    else:
                        print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                        continue
                elif not letters_guessed_input in secret_word:
                    letters_guessed += letters_guessed_input
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            break
        elif len(letters_guessed_input) > 1 or len(letters_guessed_input) == 0:
            warnings_left -= 1
            if warnings_left >= 0:
                print("Oops! That is not a valid letter. You have " + str(warnings_left) + " warnings left: "
                      ,get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: "
                      ,get_guessed_word(secret_word, letters_guessed))
                continue
        elif not letters_guessed_input in all:
            warnings_left -= 1
            if warnings_left >=0:
                print("Oops! That is not a valid letter. You have " + str(warnings_left) + " warnings left: "
                      , get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no  warnings left so you lose one guess: "
                      , get_guessed_word(secret_word, letters_guessed))
                continue
        elif letters_guessed_input in letters_guessed:
            warnings_left -= 1
            if warnings_left >=0 :
                print("Oops! You've already guessed that letter. You have " + str(warnings_left) + " warnings left: "
                      , get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "
                      , get_guessed_word(secret_word, letters_guessed))
                continue
        elif letters_guessed_input in secret_word:
            letters_guessed += letters_guessed_input
            if is_word_guessed(secret_word, letters_guessed) == True:
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                print("-------------")
                print("Congratulations, you won!")
                print("Your total score for this game is: ", len(set(secret_word)) * guesses_left)
                break
            else:
                print("Good guess: ",get_guessed_word(secret_word, letters_guessed))
                continue
        elif not letters_guessed_input in secret_word:
            letters_guessed += letters_guessed_input
            if letters_guessed_input in vowel:
                guesses_left -=2
                print("Oops! That letter is not in my word: ",get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_left -=1
                print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
    if guesses_left <=0:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was " + secret_word)
if __name__ == "__main__":
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.read()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    ct = 0
    N = len(secretWord)
    for i in range(N):
        if secretWord[i] in lettersGuessed:
            ct += 1
    if N == ct:
        return True
    return False


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    # FILL IN YOUR CODE HERE...
    N = len(secretWord)
    out_str = ""
    for i in range(N):
        if secretWord[i] in lettersGuessed:
            out_str += secretWord[i]
        else:
            out_str += "_ "
    return out_str


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    a_str = ""
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in available_letters:
        if letter not in lettersGuessed:
            a_str += letter
    return a_str


def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.
    """
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    lettersGuessed = list()
    guess_count = 8
    while not isWordGuessed(secretWord, lettersGuessed):
        if guess_count == 0:
            print("Sorry, you ran out of guesses. The word was " + str(secretWord))
            return
        print("-------------")
        print("You have " + str(guess_count) + " left")
        print("Available Letters: " + (getAvailableLetters(lettersGuessed)))
        letter = input("Please guess a letter: ")
        letter = letter.lower()
        if letter in lettersGuessed:
            print(
                "Oops! You've already guessed that letter: "
                + str(getGuessedWord(secretWord, lettersGuessed))
            )
            continue
        else:
            lettersGuessed.append(letter)
            if letter not in secretWord:
                guess_count -= 1

                print(
                    "Oops! That letter is not in my word: "
                    + str(getGuessedWord(secretWord, lettersGuessed))
                )
            else:
                print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
    print("-------------")
    print("Congratulations, you won!")

    return


wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
print(secretWord)
hangman(secretWord)

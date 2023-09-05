# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

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
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    d={}
    for a in secretWord:
        if a in lettersGuessed:
            d[a]=True
        else:
            d[a]=False
    for a in secretWord:
        if d[a]==False:
            return False
            break
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    b=''
    for a in secretWord:
        if a in lettersGuessed:
            b=b+a
        else:
            b=b+"_"
    return b



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    d=''
    import string
    for a in string.ascii_lowercase:
        if a not in lettersGuessed:
            d+=a
    return d

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    l=len(secretWord)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(l)+" letters long" )
    print("-------------")
    NoOfGuesses=8
    lettersGuessed=[]
    gw=''
    while NoOfGuesses>0 and (isWordGuessed(secretWord, lettersGuessed))==False:
        print("You have "+str(NoOfGuesses)+" guesses left")
        AvailableLetters=getAvailableLetters(lettersGuessed)
        print("Available letters: "+AvailableLetters)
        letter=input("Please guess a letter: ")
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: "+gw)
        else:
            lettersGuessed.append(letter)
            
        GuessedWord=''
        GuessedWord+=(getGuessedWord(secretWord, lettersGuessed))
        if letter in AvailableLetters:
            if letter in secretWord:
                print("Good guess: "+ GuessedWord)
            else:
                print("Oops! That letter is not in my word: "+GuessedWord)
                NoOfGuesses-=1  
        print("-----------")
        gw=GuessedWord
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was "+secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord =chooseWord(wordlist).lower()
hangman(secretWord)

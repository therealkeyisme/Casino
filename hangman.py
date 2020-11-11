from nltk.corpus import words
import random


def DecideDashes(dash, word, guess):
    emptystring = ''
    if guess in word:
        dash = list(dash)
        word = list(word)
        for i in range(len(word)):
            if word[i] == guess:
                dash[i] = guess
    return emptystring.join(dash)


def WordDecider():
    word_list = words.words()
    maxi = len(word_list)
    word = word_list[random.randint(0, maxi)]
    return word


def InitialDashes(word):
    blankstring = ""
    dashes = []
    for char in word:
        dashes.append('-')
    return(blankstring.join(dashes))


def GuessedLetters(availableletters, guess):
    blankstring = ""
    letters = []
    for char in availableletters:
        if char == guess:
            letters.append('-')
        else:
            letters.append(char)
    return blankstring.join(letters)


def hangman():
    word = WordDecider()
    print("The word to guess has {0} letters".format(len(word)))
    correct = False
    guessesLeft = 7
    availableLetters = 'abcdefghijklmnopqrstuvwxyz'
    dashInitial = InitialDashes(word)
    dashes = dashInitial

    while correct == False:

        print(dashes)
        print("Available letters: {0}".format(availableLetters))
        print("{0} incorrect guesses remaining.".format(str(guessesLeft)))
        userGuess = input("Please enter your guess:")

        if userGuess in word:
            print("Nice! {0} is in the word.".format(userGuess))
        else:
            guessesLeft -= 1
            print(
                "{0} is not in the word. Too bad. {1} incorrect guesses remaining".format(userGuess, str(guessesLeft)))

        availableLetters = GuessedLetters(availableLetters, userGuess)
        dashes = DecideDashes(dashes, word, userGuess)

        if dashes == word:
            correct = True
            print("You won the game! The word of the game was {0}".format(word))
        if guessesLeft == 0:
            print("You lost the game. The word was {0}".format(word))
            break
from craps import craps
from blackjack import blackjack
from hangman import DecideDashes, WordDecider, InitialDashes, GuessedLetters, hangman


keepplaying = 'y'

while True:
    try:
        money = int(input("How much money do you want to spend gambling?\n"))
        while money <= 0:
            money = int(input("Please make sure your starting balance is greater than zero\n"))
        print("Okay, your new balance is ${0}\n".format(money))
        break
    except ValueError:
        print("That is not a valid input")

while keepplaying.upper() == 'Y':
    print('''Here are the games that you can play:
    Craps
    BlackJack
    hangman''')
    gameToPlay = input("What game would you like to play?\n")
    if gameToPlay == "Craps" or gameToPlay == "craps":
        money, keepplaying = craps(money)
        print(money)
    elif gameToPlay == "blackjack" or gameToPlay == "BlackJack" or gameToPlay == "Blackjack":
        money, keepplaying = blackjack(money)
    elif gameToPlay.upper() == "HANGMAN":
        hangman()
    else:
        print("That game is unavailable right now or you spelled it incorrectly. Please try again later"
              ", or learn to type.")
        break

from craps import craps
from blackjack import blackjack
from hangman import hangman
from intcheck import intcheck

keepplaying = 'y'
deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3,
            4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
message = "How much money do you want to spend gambling?"
money = intcheck(money, False, True, 0)
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
    if gameToPlay.upper() == "CRAPS":
        money, keepplaying = craps(money, deck)
        print(money)
    elif gameToPlay.upper() == "BLACKJACK":
        money, keepplaying = blackjack(money, deck)
    elif gameToPlay.upper() == "HANGMAN":
        hangman()
    else:
        print("That game is unavailable right now or you spelled it incorrectly. Please try again later"
              ", or learn to type.")
        break

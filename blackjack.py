import time
import random
from intcheck import intcheck


def handtotal(hand):
    """Analyzes the hand of the player to determine totals

    Args:
        hand (list): the cards that a player has in their hand

    Returns:
        int: The sum of the player/dealer's hand
    """
    total = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            total += int(card)
    total += aces
    while total + 10 <= 21 and aces > 0:
        total += 10
        aces -= 1
    return total


def winconditions(playertot, dealertot, balance, wager):
    """Determines if a player has won or lost the game.

    Args:
        playertot (int): total of the cards in a player's hand
        dealertot (int): total of the cards in the dealer's hand
        balance (int): current balance after a wager has been placed
        wager (int): how much money is on the line
    """
    win = 0
    tie = 0
    message = ""

    if playertot == 21:
        wager = wager * 2
    elif playertot > 21:
        win = False
    elif dealertot > 21:
        win = True
    if dealertot < 21 and playertot < 21:
        # Analyzes the various outcomes if both player's totals are below 21
        if dealertot == playertot:
            tie = True
        elif dealertot > playertot:
            win = False
        elif playertot > dealertot:
            win = True

    if win == True:
        balance = balance + (2 * wager)
        message = "You win! The dealers total was {0} and your total was {1}. This brings your balance to ${2}"
    elif tie == True:
        balance = balance + wager
        message = "You tied with the dealer. Both of your totals were {0}. This brings your balance to ${2}"
    elif win == False:
        message = "You lose. The dealer's total was {0} and your total was {1}. This brings your balance to ${2}"


    print(message.format(str(dealertot), str(playertot), str(balance)))
    return balance


def blackjack(balance, deck):
    print("Welcome to blackjack.")
    mini = 0
    maxi = 51
    wagerinputmessage = "What is your bet?\n"
    while balance > 0:
        toplay = input("Would you like to play Blackjack?\n")
        if toplay.upper() == "Y" or toplay.upper() == "YES":
            playertot = 0
            dealertot = 0
            dealercards = []
            playercards = []
            print("Okay, your current balance is {0}".format(balance))

            wager = intcheck(wagerinputmessage, True, False, balance)
            balance -= wager
            print("Your wager is ${0}, this makes your new balance ${1}".format(str(wager), str(balance)))
            while len(dealercards) < 2:
                dealercards.append(deck[random.randint(mini, maxi)])
                playercards.append(deck[random.randint(mini, maxi)])
            dealertot = handtotal(dealercards)
            playertot = handtotal(playercards)
            print("You drew a {0} and a {1}. Your total is {2}.The dealer's face up card is a {3}."
                  .format(str(playercards[1]), str(playercards[0]), str(playertot),
                          str(dealercards[0])))

            if dealertot == 21:
                print("You lose. The dealer got blackjack with {0}".format(str(dealertot)))
                balance = balance
                break
            if playertot == 21 and dealertot != 21:
                print("You win. The dealer busted with {0}".format(str(dealertot)))
                balance = wager * (5 / 2)
                break
            while playertot < 21:
                playdecision = input("Would you like to hit, stand or double your bet?\n")
                if playdecision == "hit":
                    playercards.append(deck[random.randint(mini, maxi)])
                    playertot = handtotal(playercards)
                    print("You drew a {0}. This brings your total to {1}.".format(str(playercards[-1]), str(playertot)))
                    continue
                elif playdecision == "stand":
                    break
                elif playdecision == "double":
                    balance -= wager
                    wager = wager * 2
                    playercards.append(deck[random.randint(mini, maxi)])
                    playertot = handtotal(playercards)
                    print("Becuase you doubled, your new balance is now ${2}. You drew a {0}. This brings your total to {1}.".format(str(playercards[-1]), str(playertot), str(balance)))
                    break
            print("The dealer's face down card is a {0}.".format(str(dealercards[-1])))
            while dealertot < 17:
                dealercards.append(deck[random.randint(mini, maxi)])
                dealertot = handtotal(dealercards)
                print("The dealer drew a {0}. Bringing his card total to {1}".format(str(dealercards[-1]),
                                                                                     str(dealertot)))
            balance = winconditions(playertot, dealertot, balance, wager)
        elif toplay.upper() == 'N' or toplay.upper() == 'NO':
            break
        else:
            print("That is not a valid input")
            continue
    differentgame = 0
    while differentgame != "Y" or differentgame != "N":
        differentgame = input("Would you like to play a different game?\n")
        if differentgame.upper() == "YES" or differentgame.upper() == "Y":
            differentgame = "Y"
            break
        elif differentgame.upper() == "NO" or differentgame.upper() == 'N':
            differentgame = "N"
            break
        else:
            print("This is not a valid input")
            continue

    print("Come back soon!")
    return balance, differentgame

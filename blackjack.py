import time
import random


def handtotal(hand):
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


def blackjack(balance):
    print("Welcome to blackjack.")
    mini = 0
    maxi = 51
    deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3,
            4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    dealercards = []
    playercards = []
    while balance > 0:
        toplay = input("Would you like to play Blackjack?\n")
        if toplay.upper() == "Y" or toplay.upper() == "YES":
            print("Okay, your current balance is {0}".format(balance))
            while True:
                try:
                    wager = int(input("What is your bet?\n"))
                    while wager > balance:
                        wager = int(input("Your wager cannot be higher than your bank balance(${0}), please enter a "
                                          "different wager price\n".format(str(balance))))
                    while wager < 0:
                        wager = int(input("Your wager cannot be negative, please enter a different wager value\n"))
                    originalbalance = balance
                    balance = balance - wager
                    break
                except ValueError:
                    print("Your entry must be a numerical value!!")
            print("Your wager is ${0}, this makes your new balance ${1}".format(str(wager), str(balance)))
            while len(dealercards) < 2:
                dealercards.append(deck[random.randint(mini, maxi)])
                playercards.append(deck[random.randint(mini, maxi)])
            dealertot = handtotal(dealercards)
            playertot = handtotal(playercards)
            print("You drew a {0} and a {1}. Your total is {2}.The dealer's face up card is a {3}."
                  .format(str(playercards[1]), str(playercards[0]), str(playertot),
                          str(dealercards[0]), str(dealertot)))

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
                    print("You drew a {0}. This brings your total to {1}.".format(str(playercards[-1]), str(playertot)))
                    break
            print("The dealer's face down card is a {0}.".format(str(dealercards[-1])))
            while dealertot < 17:
                dealercards.append(deck[random.randint(mini, maxi)])
                dealertot = handtotal(dealercards)
                print("The dealer drew a {0}. Bringing his card total to {1}".format(str(dealercards[-1]),
                                                                                     str(dealertot)))
            if dealertot != 21 and playertot == 21:
                balance = balance + (2 * wager)
                print("You win! The dealers total was {0} and your total was {1}. This brings your balance to ${2}"
                      .format(str(dealertot), str(playertot), str(balance)))
            elif (dealertot <= 21 and playertot <= 21) and dealertot == playertot:
                balance = originalbalance
                print("You tied. The dealers total was {0} and your total was {1}. This brings your balance to ${2}"
                      .format(str(dealertot), str(playertot), str(balance)))
            elif dealertot > 21 and playertot < 21:
                balance = balance + (2 * wager)
                print("You win! The dealers total was {0} and your total was {1}. This brings your balance to ${2}"
                      .format(str(dealertot), str(playertot), str(balance)))
            elif dealertot > playertot:
                balance = balance + (2 * wager)
                print("You lost. The dealers total was {0} and your total was {1}. This brings your balance to ${2}"
                      .format(str(dealertot), str(playertot), str(balance)))
            elif dealertot < playertot:
                balance = balance + (2 * wager)
                print("You win! The dealers total was {0} and your total was {1}. This brings your balance to ${2}"
                      .format(str(dealertot), str(playertot), str(balance)))
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

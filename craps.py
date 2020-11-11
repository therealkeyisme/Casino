import random
import time


def craps(balance):
    print('''Welcome to Craps!!\nIn Craps, a player rolls two dice. Each die has six faces. These faces contain 1, 2, 3, 
    4, 5, and 6 spots. After the dice have come to rest, the sum of the spots on the two upward faces is calculated. If 
    the sum is 7 or 11 on the first throw, the player wins. If the sum is 2, 3, or 12 on the first throw (called 
    "craps"), the player loses (i.e. the "house" wins). If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
    then the sum becomes the players "point." To win, you must continue rolling the dice until you "make your point." 
    The player loses by rolling a 7 before making the point.''')
    maxi = 6
    mini = 1
    while balance > 0:
        playornot = input("Would you like to play craps 'Y' or 'N'? \n")
        if playornot == "N" or playornot == "n":
            print("You have decided to stop playing.\n")
            break
        elif playornot == "Y" or playornot == "y":
            while True:
                try:
                    wager = int(input("How much money are you willing to gamble away?"
                                      "Your balance is {0}.\n".format(str(balance))))
                    while wager > balance:
                        wager = int(input("Your wager cannot be higher than your bank balance(${0}), please enter a  "
                                          "different wager price\n".format(str(balance))))
                    while wager < 0:
                        wager = int(input("Your wager cannot be negative, please enter a different wager value\n"))
                    balance = balance - wager
                    break
                except ValueError:
                    print("That is not an integer, please enter an integer")

            print("Your new balance is {0}. Let's begin the game!".format(str(balance)))
            time.sleep(1)
            diceone = random.randint(mini, maxi)
            dicetwo = random.randint(mini, maxi)
            dicetot = diceone + dicetwo
            print("You rolled a {0}. ".format(str(dicetot)))
            if dicetot == 7 or dicetot == 11:
                "You win!!"
                balance = balance + (wager * 2)
                print("Your new balance is {0}.".format(str(balance)))
            elif dicetot == 2 or dicetot == 3 or dicetot == 12:
                "You Lost :(\nWant to try again?"
                balance = balance
                print("Your new balance is {0}.".format(str(balance)))
            else:
                print("Because you rolled a {0}, you must continue rolling the dice until you reach your original "
                      "number.".format(str(dicetot)))
                while dicetot > 0:
                    wagernew = 0
                    while True:
                        try:
                            wagernew += int(input("Would you like to add more money to your wager? You can add up to "
                                                  "{0} to your wager.".format(str(balance))))
                            while wagernew > balance:
                                wagernew = int(input("Your wager cannot be higher than your bank balance(${0}), please "
                                                     "enter a different wager price".format(str(balance))))
                            while wagernew < 0:
                                wagernew = int(input("Your wager cannot be a negative number, please enter a different "
                                                     "wager price"))
                            break
                        except ValueError:
                            print("That is not an integer, please enter an integer.")
                    balance -= wagernew
                    wager += wagernew
                    time.sleep(1)
                    diceone = random.randint(mini, maxi)
                    dicetwo = random.randint(mini, maxi)
                    losttot = diceone + dicetwo
                    print("You rolled a {0}. ".format(str(losttot)))
                    time.sleep(1)
                    if losttot == 7:
                        print("You have lost")
                        print("Your new balance is {0}.".format(str(balance)))
                        break
                    elif losttot == dicetot:
                        print("You win!")
                        balance = balance + (wager * 2)
                        print("Your new balance is {0}.".format(str(balance)))
                        break
                    else:
                        continue
        else:
            print("This is not a valid input, try again using the characters 'Y' or 'N'")
            continue
    differentgame = 0
    while differentgame != "Y" or differentgame != "N":
        differentgame = input("Would you like to play a different game?")
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

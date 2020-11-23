def intcheck(message, checkbal, addmoney, balance):
    """This checks to see if the numbers that are input to various functions are in fact, itnegers

    Args:
        message (string): the requested value
        checkbal (bool): states if the function needs to check the balance (wager)
        addmoney (bool): for when the user is stating how much money they want to gamble for
        balance (int): The balance that wants to be changed

    Returns:
        [int]: a valid integer input for the function
    """
    while True:
        try:
            output = int(input(message))
            if checkbal:
                while output > balance:
                    output = int(input("Your wager cannot be higher than your bank balance(${0}), please enter a "
                                       "different wager price\n".format(str(balance))))
                while output < 0:
                    output = int(input("Your wager cannot be negative, please enter a different wager value\n"))
                break
            if addmoney:
                while output <= 0:
                    output = int(input("Please make sure your balance is above zero.\n"))
                break
        except ValueError:
            print("Your entry must be a number")
    return output

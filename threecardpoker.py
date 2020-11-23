

def threecardpoker(balance, deck):
    print("Welcome to Three Card Poker")
    mini = 0
    maxi = 51
    
    while balance > 0:
        toplay = input("Would you like to play Three Card Poker?")

        if toplay.upper() == 'Y' or toplay.upper() == 'YES':
            print(f"Okay, your current balance is {balance}")
        
        elif toplay.upper() == 'N' or toplay.upper() == 'NO':
            pass
        else:
            pass
import random
newgame = 0

my_list = [2, 3, 4, 5 ,6 ,7, 8, 9 ,'J' ,'Q' ,'K']
def get_card():
    return random.choice(my_list)

# a = get_card() #try
# print(a)      #try

def player():
    condition = False
    total = 0
    card1 = get_card()
    card2 = get_card()

    # If anyone of them is comes, then value will be 10
    if card1 == 'J' or card1 == 'K' or card1 == 'Q':
        card1 = 10
    if card2 == 'J' or card2 == 'K' or card2 == 'Q':
        card2 = 10
        total = card1 + card2
    else:
        total = card1 + card2

    print("Player has: " + str(card1) + "and" + str(card2))
    
# player() #try

    if total == 21:
        condition = True

    while total < 21:
        choice = input('Type "S" to Stand  or "H" to hit (call for more card)')
        if choice == 's' or choice == 'S':
            break
        card1 = get_card()
        if card1 == 'J' or card1 == 'K' or card1 == 'Q':
            card1 = 10
            print("Next card Drawn Number: " + str(card1))
            total += card1
        else:
            total += card1
        print("Total: " + str(total))
    return total, condition
# player()

# =============================================================================

def dealer():

    total = 0
    card1 = get_card()
    card2 = get_card()

    # If anyone of them is comes, then value will be 10
    if card1 == 'J' or card1 == 'K' or card1 == 'Q': 
        card1 = 10
    if card2 == 'J' or card2 == 'K' or card2 == 'Q':
        card2 = 10
        total = card1 + card2
    else:
        total = card1 + card2
    print("Dealer's has: " + "X" + " " + str(card2))

    while total <= 16:
        input('Press <enter> to continue ...')
        card1 = get_card()
        if card1 == 'J' or card1 == 'K' or card1 == 'Q':
            card1 = 10
            total += card1
        else:
            total += card1
        print("\n Dealer's Drawn Card value: " + str(card1))
        print("Total: " + str(total))
    return total


def main():
    try_again = True

    while try_again:
        player_total, condition = player()
        player_wins = False
        dealer_wins = False 
        if condition:
            print('Player is winner')
            player_wins = True

        if player_total > 21:
            print(f'Player is Busted, The sum is {player_total}')
            dealer_wins = True

        if player_wins is False and dealer_wins is False:
            dealer_total = dealer()
            if player_total == dealer_total:
                print("Both sum are equal, match draw")
            if dealer_total > 21:
                print(f'Dealer is Busted, The sum is {dealer_total}')
                player_wins = True
            elif player_total > dealer_total:
                player_wins = True
            else:
                dealer_wins = True

        print("\n********** GAME OVER **********")
        if player_wins:
            print(f'Player is winner. Player sum = {player_total}, Dealer sum = {dealer_total}')
        elif dealer_wins:
            print(f'Player is Busted, because player sum is {player_total}')
        while True:
            try_again = input('Type "P" to play again or "Q" to quit the game:')
            if try_again == "Q" or try_again == 'q':
                print("Game ended.")
                try_again = False
                break
            elif try_again == "p" or try_again == 'P': 
                break
main()

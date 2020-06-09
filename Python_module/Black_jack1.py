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

    print("Player has: " + str(card1) + " and " + str(card2))
    dealer()
# player() #try

    if total == 21:
        condition = True

    while total < 21:
        choice = input('Do you want to Stand then press "S" or "H" to hit (call for more card)')
        if choice == 's' or choice == 'S':
            break
        card3 = get_card()
        if card3 == 'J' or card3 == 'K' or card3 == 'Q':
            card3 = 10
            print("Player has: " + str(card1) + " , " + str(card2) + " and " + str(card3))  
            total += card3
        else:
            total += card3
            print("Player has: " + str(card1) + " and " + str(card2) + " and " + str(card3), "Player's Total: " + str(total))  

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
    print("Dealer has: " + str(card1) + " and " + str(card2))

    while total <= 17:
        input('Dealer Turn -> /nPress <enter> to continue ...')
        card3 = get_card()
        if card3 == 'J' or card3 == 'K' or card3 == 'Q':
            card3 = 10
            print("Dealer has: " + str(card1) + " " + str(card2) + " " + str(card3))
            total += card3
        else:
            total += card3
            print("Dealer has: " + str(card1) + " " + str(card2) + " " + str(card3))
    return total

def main():
    try_again = True

    while try_again:
        player_total, condition = player()
        dealer_total = dealer()
        player_wins = False
        dealer_wins = False 
        if condition:
            print('Player is winner')
            player_wins = True

        if player_total > 21:
            print(f'Player is Busted, The sum of player is {player_total} and sum of dealer is {dealer_total}')
            dealer_wins = True

        if player_wins is False and dealer_wins is False:
            dealer_total = dealer()
        
            if player_total == dealer_total:
                print("Both sum are equal, match draw")
                player_wins = False
                dealer_wins = False    
            if dealer_total > 21:
                print(f'Dealer is Busted, The sum is {dealer_total}')
                player_wins = True

            elif player_total > dealer_total:
                player_wins = True

            else:
                dealer_wins = True

        print("\n-------GAME ENDED---------")

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

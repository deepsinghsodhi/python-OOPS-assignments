import random

player_cards= []
dealer_cards= []

my_list = [2,3,4,5,6,7,8,9,'J','Q','K','A']*4


#Dealer Cards
while len(dealer_cards) <= 2:
    dealer_cards.append(random.choice(my_list))
    print(dealer_cards[0])
    if len(dealer_cards) == 2:
        print('The Dealer has X &',dealer_cards[1])

#Dealer sum

# if sum(dealer_cards) == 21:
#     print('The Dealer has 21 and wins.')
# elif sum(dealer_cards) > 21:
#     print('The Dealer has busted.')
'''
#Player Cards
while len(player_cards) != 2:
    player_cards.append(random.choice(my_list))
    if len(player_cards) ==2:
        print('The Player has', player_cards[0],'&',player_cards[1])




#Player sum

while sum(player_cards) < 21:
    question = str(input('Do you want to stay then press Y else press any key:'))
    if question != 'Y':
        player_cards.append(random.choice(my_list))
        print('The Player now has a total of '+str(sum(player_cards))+ ' from these cards',player_cards)
    else:
        print('The Dealer has a total of '+str(sum(dealer_cards))+ ' with',dealer_cards)
        print('The Player has a total of '+str(sum(player_cards))+ ' with',player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print('Dealer wins')
        else:
            print('Player wins')
            break

if sum(player_cards) > 21:
    print('Player Busted. Dealer wins')
elif sum(player_cards) == 21:
    print('Player wins the game.')
'''
import random
dealer_cards = []
player_card = []
my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


def calculation(list1):
    total = 0
    for i in range(len(list1)):
        if list1[i] == 'J' or list1[i] == 'K' or list1[i] == 'Q':
            list1[i] = 10
        if total <= 9:
            if list1[i] == 'A':
                list1[i] = 11
        else:
            if list1[i] == 'A':
                list1[i] = 1

    for i in list1:
        total = total + i
    
    for i in range(len(list1)):
        if list1[i] == 10:
            list1[i] = 'J' or list1[i] == 'Q' or list1[i] == 'K'
        if list1[i] == 1:
            list1[i] = 'A'

    return total

def win_comb():
    if calculation(player_card) > 21:
        print("Player is busted because sum =", calculation(player_card))
        print("Dealer is winner with sum =", calculation(dealer_cards))

    elif calculation(dealer_cards) > calculation(player_card):
        print("Dealer is winner with sum =", calculation(dealer_cards))
        print("Player is loser with sum =", calculation(player_card))

    elif calculation(dealer_cards) < calculation(player_card) and calculation(player_card)<=21:
        print("Player is winner with sum =", calculation(player_card))
        print("Dealer is loser with sum =", calculation(dealer_cards))
    else:
        print("No winner with sum =", calculation(dealer_cards))

    print("_______________________Game End__________________________")

def main():
    
    print("-*-*-*-*-*-*-*-*-Welcome to Black Jack!-*-*-*-*-*-*-*-*-")
    
    # For Dealer Condition and card selection ----------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    while (len(dealer_cards) < 3 ):
            random_element = random.randrange(len(my_list))
            k = my_list[random_element]
            dealer_cards.append(k)
            my_list.pop(random_element)
            if len(dealer_cards) == 2 and calculation(dealer_cards) >= 16 :
                print("Dealer has cards X and", dealer_cards[1])
                break

            if len(dealer_cards) == 2 and calculation(dealer_cards) < 16:
                            condition = True
                            while condition:
                                random_element1 = random.randrange(len(my_list))
                                element = my_list[random_element1]
                                dealer_cards.append(element)
                                if calculation(dealer_cards) >= 16 and calculation(dealer_cards) < 21:
                                    my_list.pop(random_element1)
                                    print("Dealer has cards X", dealer_cards[1], "and", dealer_cards[2])
                                    condition = False

                                else:
                                    dealer_cards.pop(2)
                                    continue

    # For Player Condition and card selection ----------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    while len(player_card) < 3:
            random_element = random.randrange(len(my_list))
            k = my_list[random_element]
            player_card.append(k)
            my_list.pop(random_element)
            if len(player_card) == 2:
                print("Player has cards", player_card[0], " and ", player_card[1])
                print('_' * 40)
                options = input("Enter H / h for more card or S / s for close:")
                if options == "H" or options == 'h':
                    random_element1 = random.randrange(len(my_list))
                    p = my_list[random_element1]
                    player_card.append(p)
                    my_list.pop(random_element1)
                    print("Player has", player_card[0],",",player_card[1],"and", player_card[2])
                elif options == "S" or options == 's': #Breaking the while loop.
                    break
    win_comb()
main()

import random
dealer_cards = []
my_cards = []
my_list = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

def win():
    if calc(my_cards) > 21:
        print("Player is busted because sum =",calc(my_cards))
        print("Dealer is winner with sum =",calc(dealer_cards))

    elif calc(dealer_cards) > calc(my_cards):
        print("Dealer is winner with sum =", calc(dealer_cards))
        print("Player is loser with sum =", calc(my_cards))
    elif calc(dealer_cards) < calc(my_cards) and calc(my_cards)<=21:
        print("Player is winner with sum =", calc(my_cards))
        print("Dealer is loser with sum =", calc(dealer_cards))
    else:
        print("No winner with sum =",calc(dealer_cards))

    print("-------Game Ends--------")


def calc(list1):
    sum1 = 0
    for i in range(len(list1)):
        if list1[i] == 'J':
            list1[i] = 10
        if list1[i] == 'K':
            list1[i] = 10
        if list1[i] == 'Q':
            list1[i] = 10
        if list1[i] == 'A':
            list1[i] = 11


    for i in list1:
        sum1 = sum1 +i

    for i in range(len(list1)):
        if list1[i] == 10:
            list1[i] = 'J' or list1[i] == 'Q' or list1[i] == 'K'
        if list1[i] == 1:
            list1[i] = 'A'

    return sum1



def game():
    print("---------Welcome to Black Jack game---------")
    while (len(dealer_cards) <3 ):
            rand_idx = random.randrange(len(my_list))
            k = my_list[rand_idx]
            dealer_cards.append(k)
            my_list.pop(rand_idx)
            if len(dealer_cards) == 2 and calc(dealer_cards) >= 16 :
                print("Dealer has cards X and ",dealer_cards[1])
                break

            if len(dealer_cards) == 2 and calc(dealer_cards)<16: #based on black jack dealer rules if sum <16 then dealer has three cards
                            condition = True
                            while(condition):
                                rand_idx1 = random.randrange(len(my_list))
                                p = my_list[rand_idx1]
                                dealer_cards.append(p)
                                if calc(dealer_cards)>=16 and calc(dealer_cards)<21:
                                    #dealer_cards.append(p)
                                    my_list.pop(rand_idx1)
                                    print("Dealer has cards X",dealer_cards[1], dealer_cards[2])
                                    condition = False

                                else:
                                    dealer_cards.pop(2)
                                    continue


    while (len(my_cards)<3):
            rand_idx = random.randrange(len(my_list))
            k = my_list[rand_idx]
            my_cards.append(k)
            my_list.pop(rand_idx)
            if len(my_cards) == 2:
                print("Player has cards",my_cards[0],my_cards[1])
                input1 = input("Enter Hit or Stand:")
                if input1 == "Hit":
                    rand_idx1 = random.randrange(len(my_list))
                    p = my_list[rand_idx1]
                    my_cards.append(p)
                    my_list.pop(rand_idx1)
                    print("Player has",my_cards[0],my_cards[1],my_cards[2])

                elif input1 == "Stand":
                    break

    win()

game()
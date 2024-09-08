import random
import art

def deal_card_f(lst):
    return random.choice(lst)

def calculate_score_f(l1):
    score = sum(l1)
    if len(l1)==2 and score==21:
        return 0
    elif 11 in l1 and score>21:
        l1.remove(11)
        l1.append(1)
        return sum(l1)
    else:
        return score

def drawing(p_card,c_card,deal_card,calculate_score):
    draw=True
    while draw:
        print(f"    Your cards: {p_card}, current score: {calculate_score   (p_card)}")
        print(f"    Computer's first card: {c_card[0]}")
        if calculate_score(p_card)>21:
            draw=False
            print("You went over. You Loose!!!")
        elif calculate_score(c_card) > 21:
            draw=False
            print("Opponent went over. You Win!!!")
        elif calculate_score(c_card)==0:
            draw=False
            print("Computer got a Blackjack. You Loose!!!")
        elif calculate_score(p_card)==0:
            draw=False
            print("You got a Blackjack. You Win!!!")
        else:
            cont=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if cont=='y':
                p_card.append(deal_card(cards_list))
                if calculate_score(c_card)<17:
                    c_card.append(deal_card(cards_list))
            else:
                draw=False
                print(f"    Your final hand: {p_card}, final score: {calculate_score(p_card)}")
                print(f"    Computer's final hand: {c_card}, final score: {calculate_score(c_card)}")


                if calculate_score(p_card)>calculate_score(c_card) or calculate_score(p_card)==0 :
                    print("You Win!!!")
                elif calculate_score(p_card) < calculate_score(c_card):
                    print("You Loose!!!")
                else:
                    print("Draw!!!")


play_again=True
while play_again:
    cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_card = []
    computer_card = []
    for i in range(2):
        player_card.append(deal_card_f(cards_list))
        computer_card.append(deal_card_f(cards_list))
    print(art.logo)
    drawing(player_card,computer_card,deal_card_f,calculate_score_f)
    play=input("Do you want to play again 'y'/'n': ").lower()
    if play=='n':
        play_again=False
    else:
        print("\n" * 20)






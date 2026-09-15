from DeckOfCards import *

def calc_score(cards):
    """Caluculates the total score of cards, adjusting for Ace (11 to 1) If necessary"""
    score = 0
    ace_count = 0

    for card in cards:
        score +=card.val
        if card.face == 'Ace':
            ace_count += 1
    # Automatically reduce score by 10 if score exceeds 21 and an Ace is present
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

print("Welcome to Black Jack!")

# define DeckOfCards object from DeckOfCards.py
deck = DeckOfCards()

# Main game loop allowing multiple rounds with the same deck
playgame = True
while playgame:
    print("\ndeck before shuffled:")
    deck.print_deck()
    print("\ndeck after shuffled:")
    deck.shuffle_deck()
    deck.print_deck()
    # define two lists to score cards
    user_cards = []
    dealer_cards = []


    # deal two cards to the user and add the user list
    card = deck.get_card()
    print("\nCard number 1 is:", card)
    user_cards.append(card)
    card2 = deck.get_card()
    print("Card number 2 is:", card2)
    user_cards.append(card2)

    # calculate user's score
    score = calc_score(user_cards)
    print("Your socre is:", score)

    
    # ask user if they would like a "hit" (another card)
    hit = str(input("would you like a hit?(y/n) "))
    card_number = 2
    while hit == 'y':
        card_number += 1
        card3 = deck.get_card()
        print("Card number",str(card_number),"is:",card3)
        # add a card to user list and score it
        user_cards.append(card3)
        score = calc_score(user_cards)
        print("Your total socre is: ", score)
        if score > 21:
            break
        hit = str(input("would you like a hit?(y/n) "))

    # Check game outcome for user and handle dealer turn if user didn't bust
    if score > 21:
        print("User burst! You lose!")
    else: 
        # Deal two cards to the dealer
        dcard1 = deck.get_card()
        print("Dealer card number 1 is:", dcard1)
        dealer_cards.append(dcard1)
        dcard2 = deck.get_card()
        print("Dealer card number 2 is:", dcard2)
        dealer_cards.append(dcard2)


        dcard_number = 2
        dealer_score = calc_score(dealer_cards)

        # Dealer must hit while score is under 17
        while dealer_score < 17:
            dcard_number += 1
            dcard3 = deck.get_card()
            print("Dealer hits, card number" , str(dcard_number) ,"is:" , dcard3)
            dealer_cards.append(dcard3)
            dealer_score =calc_score(dealer_cards)
            print("Dealer score is:" ,str(dealer_score))

        # Compare scores and determine the winner
        if dealer_score > 21:
            print("Dealer busted, you win!")
        elif score > dealer_score:
            print("Your score is higher, you win!")
        elif score < dealer_score:
            print("Dealer score is higher, you lose!")
        else:
            print("Dealer score is equal, you lose!")
    # Ask the user if they want to play another game
    endgame=input("another game?(y/n)")
    print()

    if endgame == 'n':
        playgame = False

    
    
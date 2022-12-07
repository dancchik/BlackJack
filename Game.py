from Deck import Deck, Chips
from Player import Player
from Functions import *

playing = True

# Gameplay!

while True:
    print("Welcome to BlackJack!")

    # create an shuffle deck
    deck = Deck()
    deck.shuffle()

    player_hand = Player()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Player()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up the player's chips
    player_chips = Chips()

    # ask player for bet
    take_bet(player_chips)

    # show cards
    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

    print("\nPlayer's winnings stand at", player_chips.total)

    new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break

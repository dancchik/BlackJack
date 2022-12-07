# FUNCTIONS

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry! Please can you type in a number: ")
        else:
            if chips.bet > chips.total:
                print("You bet can't exceed 100!")
            else:
                break


def hit(deck, player):
    player.add_card(deck.deal())
    player.adjust_for_ace()


def hit_or_stand(deck, hand):   # hit or stand
    global playing

    while True:
        ask = input("\nWould you like to hit or stand? Please enter 'h' or 's': ")

        if ask[0].lower() == 'h':
            hit(deck, hand)
        elif ask[0].lower() == 's':
            print("Player stands, Dealer is playing.")
            playing = False
        else:
            print("Sorry! I did not understand that! Please try again!")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand: ")
    print(" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


# game endings

def player_busts(player, dealer, chips):
    print("PLAYER BUSTS!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("DEALER BUSTS!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push(player, dealer):
    print("Its a push! Player and Dealer tie!")


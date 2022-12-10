##      NET 2008        ASSIGNMENT 4
##      ALEX VOHSEMER

import requests

SHUFFLE_URL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
DRAW_URL = "https://deckofcardsapi.com/api/deck/{}/draw/?count=1"

def shuffleDeck():
    
    return ((requests.get(SHUFFLE_URL).json())['deck_id'])



def drawCard(deck_id):
    
    value = (requests.get(DRAW_URL.format(deck_id)).json())['cards'][0]['value']
    
    if (value == 'JACK'):
        value = 11
    if (value == 'QUEEN'):
        value = 12
    if (value == 'KING'):
        value = 13
    if (value == 'ACE'):
        value = 14
        
    return int(value)



playing = True

while playing:
    
    NPC_DECK_ID = shuffleDeck()
    USER_DECK_ID = shuffleDeck()

    user_wins = 0
    NPC_wins = 0

    cards_remaining = 52

    input("Welcome to War! Press ENTER to continue.")
    while (cards_remaining > 1):
        
        NPC_CARD = drawCard(NPC_DECK_ID)
        USER_CARD = drawCard(USER_DECK_ID)

        print("")
        print("Your card was:                       " + str(USER_CARD))
        print("The dealer's card was:       " + str(NPC_CARD))
        
        if (USER_CARD > NPC_CARD):
            print("You won!")
            user_wins += 1

        if (USER_CARD < NPC_CARD):
            print("You lost!")
            NPC_wins += 1

        if (USER_CARD == NPC_CARD):
            print("It's a tie!")

        input("Press ENTER to continue.")
        cards_remaining -= 1

    print("")
    print("Your wins: " + str(user_wins))
    print("NPC's wins: " + str(NPC_wins))

    if (user_wins > NPC_wins):
        print("You won the game of War!")

    if (user_wins < NPC_wins):
        print("You lost the game of War!")

    if (user_wins == NPC_wins):
        print("You tied the game of War!")
    
    print("You're out of cards! Play again?")
    print("")



    

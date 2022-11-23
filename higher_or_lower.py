# HigherOrLower
import random

# Card constants
suit_tuple = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
rank_tuple = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

ncards = 8

# Pass in a deck and this function returns a random card form the deck
def get_card(deck_list_in):
    this_card = deck_list_in.pop() # Pop one off the top of the deck and return
    return this_card

# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deck_list_in):
    deck_list_out = deck_list_in.copy()
    random.shuffle(deck_list_out)
    return deck_list_out

# Main code
print('Welcome to Higher or Lower')
print('Choose whether the next card to be shown will be highter or lower than the current card.')
print('Earn 20 points if you get it right; lose 15 points if you get it wrong.')
print('You have 50 points to start.')

starting_deck_list = []
for suit in suit_tuple:
    for value, rank in enumerate(rank_tuple):
        card_dict = {'rank': rank, 'suit': suit, 'value': value + 1}
        starting_deck_list.append(card_dict)

score = 50

while True: # Play multiple games
    print()
    game_deck_list = shuffle(starting_deck_list)
    current_dict = get_card(game_deck_list)
    current_rank = current_dict['rank']
    current_value = current_dict['value']
    current_suit = current_dict['suit']
    print('Starting card is:', current_rank + ' of ' + current_suit)
    print()

    for card_num in range (0, ncards): # Play one game of this many cards
        answer = input(f'Is the next card higher or lower than the {current_rank} of {current_suit}? (enter h or l): ')
        answer = answer.casefold() # force lowercase
        next_card_dict = get_card(game_deck_list)
        next_card_rank = next_card_dict['rank']
        next_card_suit = next_card_dict['suit']
        next_card_value = next_card_dict['value']
        print(f'Next card is: {next_card_rank} of {next_card_suit}')

        if answer == 'h':
            if next_card_value > current_value:
                print('Right! It was higher.')
                score += 20
            else:
                print('Sorry, it was not higher.')
                score -= 15
        elif answer == 'l':
            if next_card_value < current_value:
                print('Right! It was lower.')
                score += 20
            else:
                print('Sorry, it was not lower.')
                score -= 15
        
        print(f'Your score is: {score}')
        print()
        current_rank = next_card_rank
        current_value = next_card_value
    
    go_again = input('Press ENTER to play again, or \"q\" to quit: ')
    if go_again == 'q':
        break

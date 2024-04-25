import random

num_players = 4
player_hands = []
current_player = 0
deck = ['Wachter', 'Wachter', 'Wachter', 'Wachter', 'Wachter','Priester','Priester','Baron','Baron','Kamermeisje','Kamermeisje','Prins','Prins','Koning','Gravin','Prinses']

def init():
    random.shuffle(deck)
    for i in range(num_players):
        player_hands.append([])

def deal_cards():
    for player in range(num_players):
        player_hands[player].append(deck.pop())

def print_hands():
    print("deck:",player_hands)
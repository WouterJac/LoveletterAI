import random


class GameLogic:
    def __init__(self):
        self.num_players = 4
        self.players_left = self.num_players
        self.player_hands = []
        self.current_player = 0
        self.deck = [
            "Wachter",
            "Wachter",
            "Wachter",
            "Wachter",
            "Wachter",
            "Priester",
            "Priester",
            "Baron",
            "Baron",
            "Kamermeisje",
            "Kamermeisje",
            "Prins",
            "Prins",
            "Koning",
            "Gravin",
            "Prinses",
        ]
        random.shuffle(self.deck)
        for i in range(self.num_players):
            self.player_hands.append([])
        self.deal_cards()

    def deal_cards(self):
        for player in range(self.num_players):
            self.player_hands[player].append(self.deck.pop())

    def deal_card(self):
        self.player_hands[current_player].append(self.deck.pop())

    def advance_turn(self):
        global current_player
        current_player = current_player + 1 % self.num_players

    def print_hands(self):
        print("All player cards:")
        for player in range(self.num_players):
            self.print_hand(player)

    def print_hand(self, player):
        print("Player ", player, " hand: ")
        hand = ""
        for card in range(len(self.player_hands[player])):
            hand = hand + str(card+1) + ") " + self.player_hands[player][card]
        print(hand)

    def game_is_over(self):
        return (not len(self.deck) > 0) | self.num_players == 1

    def end_game(self):
        print("Throwdown! End game")

    def play_turn(self):
        self.deal_card()
        self.print_hand(current_player)
        self.advance_turn()

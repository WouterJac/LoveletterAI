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
        self.player_hands[self.current_player].append(self.deck.pop())

    def advance_turn(self):
        self.current_player = self.current_player + 1 % self.num_players

    def print_hands(self):
        print("All player cards:")
        for player in range(self.num_players):
            self.print_hand(player)

    def print_hand(self, player):
        print("\nPlayer ", player, " hand: ")
        hand = ""
        for card in range(len(self.player_hands[player])):
            hand = hand + str(card+1) + ") " + self.player_hands[player][card]+" "
        print(hand)

    def game_is_over(self):
        return (not len(self.deck) > 0) | self.num_players == 1

    def end_game(self):
        print("Throwdown! End game")

    def play_turn(self):
        self.deal_card()
        self.print_hand(self.current_player)
        chosen_card = 0
        card_chosen = False
        while not card_chosen:
            try:
                chosen_card = int(input('Welke kaart wil je spelen? (1/2): '))
                if chosen_card < 1 or chosen_card > 2:
                    card_chosen = False
                    print("Please choose a valid option.\n")
                else:
                    card_chosen = True
            except ValueError:
                print("Please choose a valid option.\n")
        self.play_card(int(chosen_card-1))
        self.advance_turn()

    def play_card(self, card):
        chosen_card_str = str(self.player_hands[self.current_player][card])
        print(chosen_card_str)
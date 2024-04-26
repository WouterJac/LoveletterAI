import random


class GameLogic:
    def __init__(self):
        self.num_players = 4
        self.players_left = self.num_players
        self.player_hands = []
        self.players_lost = set()
        self.players_kamermeisje = set()
        self.current_player = 1
        self.set_aside_card = 0
        self.keuzes = {
            1: "Wachter",
            2: "Priester",
            3: "Baron",
            4: "Kamermeisje",
            5: "Prins",
            6: "Koning",
            7: "Gravin",
            8: "Prinses",
        }
        self.deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        random.shuffle(self.deck)
        for i in range(self.num_players + 1):
            self.player_hands.append([])
        self.deal_cards()

    def deal_cards(self):
        self.set_aside_card = self.deck.pop()
        for player in range(1, self.num_players + 1, 1):
            self.deal_card(player)

    def deal_card(self, player):
        self.player_hands[player].append(self.deck.pop())

    def advance_turn(self):
        self.current_player = (self.current_player % self.num_players) + 1

    def print_hands(self):
        print("All player cards:")
        for player in range(self.num_players):
            self.print_hand(player + 1)

    def print_hand(self, player):
        print("\nPlayer ", player, " hand: ")
        hand = ""
        for card in range(len(self.player_hands[player])):
            hand = (
                hand
                + str(card + 1)
                + ") "
                + self.keuzes.get(self.player_hands[player][card])
                + " "
            )
        print(hand)

    def game_is_over(self):
        return (not len(self.deck) > 0) | self.num_players == 1

    def end_game(self):
        print("Throwdown! End game")

    def player_has_lost(self, player):
        return player in self.players_lost

    def player_lose(self, player):
        self.players_lost.add(player)
        print("Player ", player, " has lost and is out of the game.")

    def countess_forced(self):
        cards = self.player_hands[self.current_player]
        if 7 in cards:
            if 5 in cards:
                return True
            if 6 in cards:
                return True
        return False

    def play_turn(self):
        print("\nPlayer ", str(self.current_player), "'s turn.")
        self.players_kamermeisje.discard(self.current_player)
        self.deal_card(self.current_player)
        self.print_hand(self.current_player)
        chosen_card = 0
        if self.countess_forced():
            chosen_card = 1 if self.player_hands[self.current_player][0] == 7 else 2
        else:
            card_chosen = False
            while not card_chosen:
                try:
                    chosen_card = int(input("Welke kaart wil je spelen? (1/2): "))
                    if chosen_card < 1 or chosen_card > 2:
                        card_chosen = False
                        print("Please choose a valid option.\n")
                    else:
                        card_chosen = True
                except ValueError:
                    print("Please choose a valid option.\n")

        self.play_card(int(chosen_card - 1))
        self.advance_turn()

    def play_card(self, card):
        chosen_card = self.player_hands[self.current_player].pop(card)
        chosen_card_str = self.keuzes.get(chosen_card)
        print(chosen_card_str)
        match chosen_card_str:
            case "Prinses":
                self.play_princess()
            case "Wachter":
                self.play_guard()
            case "Priester":
                self.play_priest()
            case "Baron":
                self.play_baron()
            case "Kamermeisje":
                self.play_kamermeisje()
            case "Prins":
                self.play_prins()
            case "Koning":
                self.play_king()

    def play_princess(self):
        self.player_lose(self.current_player)

    def player_protected_kamermeisje(self, player):
        return player in self.players_kamermeisje

    def choose_target_player(self, prins=False):
        print("Choose a player to target:")
        eligible_players = set()
        for player in range(self.num_players):
            if (
                not self.player_has_lost(player + 1)
                and ((player + 1 != self.current_player) or prins)
                and not self.player_protected_kamermeisje(player + 1)
            ):
                eligible_players.add(player + 1)
        print(eligible_players)

        valid_player = False
        while not valid_player:
            try:
                chosen_player = int(input())
                if chosen_player not in eligible_players:
                    valid_player = False
                    print("Please choose a valid option.")
                    print(eligible_players)
                else:
                    valid_player = True
            except ValueError:
                print("Please choose a valid option.")
                print(eligible_players)
        return chosen_player

    def get_player_card(self, player):
        return self.player_hands[player][0]

    def get_current_player_other_card(self):
        return self.player_hands[self.current_player][0]

    def discard_hand(self, player):
        self.player_hands[player].pop()
        self.deal_card(player)

    def switch_hands(self, player):
        target_card = self.get_player_card(player)
        current_card = self.get_current_player_other_card()
        self.player_hands[self.current_player][0] = target_card
        self.player_hands[player][0] = current_card

    def play_guard(self):
        print("A guard was played by Player ", self.current_player)
        target = self.choose_target_player()
        guessed_a_card = False
        while not guessed_a_card:
            try:
                print("Which card do you think this player has?")
                print(self.keuzes)
                card_guess = int(input())
                if card_guess < 1 or card_guess > 8:
                    guessed_a_card = False
                    print("Please choose a valid option.\n")
                else:
                    guessed_a_card = True
            except ValueError:
                print("Please choose a valid option.\n")
        if self.player_hands[target][0] == self.keuzes.get(card_guess):
            self.player_lose(target)

    def play_priest(self):
        print("A priest was played by Player ", self.current_player)
        target = self.choose_target_player()
        print("This is the hand of player ", target, ": ")
        self.print_hand(target)

    def play_baron(self):
        print("A baron was played by Player ", self.current_player)
        target = self.choose_target_player()
        target_card = self.get_player_card(target)
        current_player_card = self.get_current_player_other_card()
        if target_card > current_player_card:
            self.player_lose(self.current_player)
        elif target_card < current_player_card:
            self.player_lose(target)
        else:
            print("The showdown was a tie.")

    def play_kamermeisje(self):
        print("A kamermeisje was played by Player ", self.current_player)
        self.players_kamermeisje.add(self.current_player)

    def play_prins(self):
        print("A prince was played by Player ", self.current_player)
        target = self.choose_target_player(prins=True)
        self.discard_hand(target)

    def play_king(self):
        print("A king was played by Player ", self.current_player)
        target = self.choose_target_player()
        self.switch_hands(target)

    def play_countess(self):
        print("A countess was played by Player ", self.current_player)

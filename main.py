import game_logic
# import visualizer


games = 1

# for game in range(games):
game_logic = game_logic.GameLogic()
game_logic.print_hands()

game_over = False
game_logic.play_turn()
game_over = game_logic.game_is_over()
game_logic.end_game()


from connectFour import ConnectFour

game = ConnectFour.new_game()
player = 1
while True:
    print(game.board_to_emoji())
    col = int(input("Enter a column number"))
    if game.play_turn(col):
        break
    player = game.active_player

print(game.board_to_emoji())

input("Player " + str(player) + " Won!!.\nPress anything to exit")




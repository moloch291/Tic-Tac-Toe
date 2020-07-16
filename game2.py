import game


def game_cycle():
    table = game.define_table()
    win_conditions = game.win_conditions()
    player1_sign = game.get_player1_sign()
    player2_sign = game.determine_player2_sign(player1_sign)
    print(table)
    for i in range(1, 10):
        if i % 2 != 0:
            table = player_turn(player1_sign, table)
        else:
            table = player_turn(player2_sign, table)
    print("No winner this time... \nCome on, this is an easy game!")


def player_turn(player_sign, table):
    mark = game.get_player_inp()
    table = game.set_mark_on_table(mark, table, player_sign)
    print(table)
    return table

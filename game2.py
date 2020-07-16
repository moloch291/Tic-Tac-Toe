import game


def game_cycle():
    table = game.define_table()
    print(table)
    win_conditions = game.get_win_conditions()
    player1_sign = game.get_player1_sign()
    player2_sign = game.get_player2_sign(player1_sign)
    table = game.define_table()
    for i in range(1, 10):
        if i % 2 != 0:
            table = player_turn(player1_sign, table, win_conditions)
        else:
            table = player_turn(player2_sign, table, win_conditions)


def player_turn(player_sign, table, win_conditions):
    mark = game.get_player_inp()
    table = game.set_mark_on_table(mark, table, player_sign)
    print(table)
    game.win_check(mark, win_conditions, table)
    print(win_conditions)
    return table

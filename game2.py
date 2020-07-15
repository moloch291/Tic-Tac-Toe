import game


def game_cycle():
    table = game.define_table()
    print(table)
    win_conditions = game.get_win_conditions()
    player1_sign = game.get_player1_sign()
    player2_sign = game.get_player2_sign(player1_sign)
    table = game.define_table()
    for i in range(9):
        if i % 2 != 0:
            mark = game.get_player_inp()
            game.set_mark_on_table(mark, table, player1_sign)
            game.win_check(mark, win_conditions)
            print(table)

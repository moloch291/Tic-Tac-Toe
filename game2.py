import game


def game_cycle():
    table = game.define_table()
    win_conditions_list = game.define_win_conditions()
    player1_sign = game.get_player1_sign()
    player2_sign = game.determine_player2_sign(player1_sign)
    print(table)
    print(win_conditions_list)
    for i in range(1, 10):
        if i % 2 != 0:
            mark = game.get_player_inp()
            table = player_turn(player1_sign, table, mark)
            win_conditions_list = game.add_sign_to_win_cons(win_conditions_list, mark, player1_sign)
            print(win_conditions_list)
        else:
            mark = game.get_player_inp()
            table = player_turn(player2_sign, table, mark)
            win_conditions_list = game.add_sign_to_win_cons(win_conditions_list, mark, player2_sign)
            print(win_conditions_list)
    print("No winner this time... \nCome on, this is an easy game!")


def player_turn(player_sign, table, mark):
    table = game.set_mark_on_table(mark, table, player_sign)
    print(table)
    return table

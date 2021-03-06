import functions


def game_cycle():
    table = functions.define_table()
    win_conditions_list = functions.define_win_conditions()
    player1_sign = functions.get_player1_sign()
    player2_sign = functions.determine_player2_sign(player1_sign)
    available_marks = functions.get_available_marks()
    print(table)
    for i in range(1, 10):
        if i % 2 != 0:
            print("Player 1:")
            mark = functions.get_player_inp()
            available_marks = functions.check_mark(mark, available_marks)
            table = player_turn(player1_sign, table, mark)
            win_conditions_list = functions.add_sign_to_win_cons(win_conditions_list, mark, player1_sign)
            functions.win_check(win_conditions_list, player1_sign)
        else:
            print("Player 2:")
            mark = functions.get_player_inp()
            available_marks = functions.check_mark(mark, available_marks)
            table = player_turn(player2_sign, table, mark)
            win_conditions_list = functions.add_sign_to_win_cons(win_conditions_list, mark, player2_sign)
            functions.win_check(win_conditions_list, player1_sign)
    print("No winner this time... \nCome on, this is an easy game!")


def player_turn(player_sign, table, mark):
    table = functions.set_mark_on_table(mark, table, player_sign)
    print(table)
    return table

import game


def game_cycle():
    table = game.define_table()
    player1_sign = game.get_player1_sign()
    player2_sign = game.get_player2_sign(player1_sign)
    print(table)
    player1_win_cons = []
    player2_win_cons = []
    for i in range(1, 10):
        if i % 2 != 0:
            table = player_turn(player1_sign, table, player1_win_cons)
        else:
            table = player_turn(player2_sign, table, player2_win_cons)
    print("No winner this time... \nCome on, this is an easy game!")
    print(player1_win_cons)
    print(player2_win_cons)


def player_turn(player_sign, table, win_cons):
    mark = game.get_player_inp()
    table = game.set_mark_on_table(mark, table, player_sign)
    for i in range(len(table)):
        if table[i] == mark:
            win_cons.append(mark)
    print(table)
    return table

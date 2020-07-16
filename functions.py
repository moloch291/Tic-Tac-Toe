def define_table():
    table = "  1 | 2 | 3 \n____|___|____ \n  4 | 5 | 6 \n____|___|____ \n  7 | 8 | 9  \n    |   |   "
    return table


def define_win_conditions():
    win_conditions_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    return win_conditions_list


def get_player1_sign():
    player1_sign = input("Player 1: choose a sign! \nIt can be 'x' or 'o'... ").upper()
    if player1_sign == "X":
        return player1_sign
    elif player1_sign == "O":
        return player1_sign
    else:
        print("Please choose and type 'x' or 'o'!")
        get_player1_sign()


def determine_player2_sign(player1_sign):
    if player1_sign == "X":
        player2_sign = "O"
    else:
        player2_sign = "X"
    print("So Player 2 has: " + player2_sign + "! \nPlayer 1 starts. ")
    return player2_sign


def get_player_inp():
    mark = input("Choose a field to mark! ")
    return mark


def set_mark_on_table(mark, table, sign):
    table = table.replace(mark, sign)
    return table


def add_sign_to_win_cons(win_conditions_list, mark, sign):
    win_conditions_list = [[str(i).replace(mark, sign) for i in win_con] for win_con in win_conditions_list]
    return win_conditions_list


def win_check(win_conditions_list, sign):
    for i in win_conditions_list:
        for w in range(len(i)):
            if i[w] == sign and i[w + 1] == sign and i[w + 2] == sign:
                print("Congratulations! " + sign + " wins!")
                quit()

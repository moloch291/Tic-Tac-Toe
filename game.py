def define_table():
    table = "  1 | 2 | 3 \n____|___|____ \n  4 | 5 | 6 \n____|___|____ \n  7 | 8 | 9  \n    |   |   "
    return table


def get_player1_sign():
    player1_sign = input("Player 1: choose a sign! \nIt can be 'x' or 'o'... ").upper()
    if player1_sign == "x".upper():
        return player1_sign
    elif player1_sign == "o".upper():
        return player1_sign
    else:
        print("Please choose and type 'x' or 'o'!")
        get_player1_sign()


def get_player2_sign(player1_sign):
    if player1_sign == "x".upper():
        player2_sign = "O"
    else:
        player2_sign = "X"
    print("So Player 2 has: " + player2_sign + "! \nPlayer 1 starts. ")
    return player2_sign


def get_player_inp():
    mark = input("Choose a field to mark! ")
    return mark


def set_mark_on_table(mark, table, sign):
    for i in range(len(table)):
        if table[i] == mark:
            table = table.replace(mark, sign)
    return table

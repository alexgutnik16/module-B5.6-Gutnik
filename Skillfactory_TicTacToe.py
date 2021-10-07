board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_is_going = True
winner = None
current_player = "X"
again = True


def game():
    global again
    while again:

        print("Добро пожловать в игру 'крестики - нолики'!")
        global game_is_going
        show_board()
        while game_is_going:

            players_turn(current_player)
            end_game_conditions()
            change_player()

        play_again()


def show_board():
    print(" Поле сейчас:", "       Номера ячеек:")
    print(" ", board[0], "|", board[1], "|", board[2], "          ", 1, "|", 2, "|", 3)
    print(" ", board[3], "|", board[4], "|", board[5], "          ", 4, "|", 5, "|", 6)
    print(" ", board[6], "|", board[7], "|", board[8], "          ", 7, "|", 8, "|", 9)
    print("-----------------------------------------------------")


def players_turn(player):
    print(f"Ходит {player}")
    position = input("Введите номер ячейки, куда вы хотите походить (1 - 9) ")
    print("-----------------------------------------------------")
    right_position = False

    while not right_position:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:

            position = input("Введите номер ячейки, куда вы хотите походить (1 - 9) ")
        position = int(position) - 1

        if board[position] != "-":
            print("Эта ячейка уже занята, введите другой номер ячейки")
        else:
            right_position = True

    board[position] = player
    show_board()


def change_player():
    global current_player
    if current_player == "X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"


def end_game_conditions():
    winning_conditions()
    tie_conditions()


def winning_conditions():
    global game_is_going
    global current_player
    if any([board[0] == board[1] == board[2] != "-",
            board[3] == board[4] == board[5] != "-",
            board[6] == board[7] == board[8] != "-",
            board[0] == board[3] == board[6] != "-",
            board[1] == board[4] == board[7] != "-",
            board[2] == board[5] == board[8] != "-",
            board[0] == board[4] == board[8] != "-",
            board[2] == board[4] == board[6] != "-"]):
        print(f"Победил {current_player}")
        game_is_going = False


def tie_conditions():
    global game_is_going
    if not winning_conditions and "-" not in board:
        print("Ничья")
        game_is_going = False


def play_again():
    global again
    global current_player
    global game_is_going
    answer = input("Хотите сыграть снова? (Да / Нет)").lower()
    if answer == "да":
        for i in range(9):
            board[i] = "-"
        current_player = "X"
        game_is_going = True
    elif answer != "да":
        print("Спасибо за игру, до свидания!")
        again = False


game()

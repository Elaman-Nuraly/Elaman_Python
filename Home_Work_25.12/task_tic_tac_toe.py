def print_board(board):
    print("-------------")
    for row in board:
        print(f"| {row[0]} | {row[1]} | {row[2]} | ")
        print("-------------")

def check_winner(board, player):
    # Проверка строк
    for row in board:
        if row.count(player) == len(row):
            return True

    # Проверка столбцов
    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    # Проверка диагоналей
    if all(board[i][i] == player for i in range(len(board))) or \
       all(board[i][len(board[0])-1-i] == player for i in range(len(board))):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def play_tic_tac_toe():
    board_size = 3
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    current_player = 'X'

    while True:
        print_board(board)

        try:
            move = int(input(f"Куда поставим {current_player}? "))
        except ValueError:
            print("Введите корректное число.")
            continue

        if move < 1 or move > 9:
            print("Введите число от 1 до 9.")
            continue

        row = (move - 1) // board_size
        col = (move - 1) % board_size

        if board[row][col] == ' ':
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"{current_player} выиграл!")
                break

            if is_board_full(board):
                print_board(board)
                print("Ничья!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Эта ячейка уже занята. Выберите другую.")

if __name__ == "__main__":
    print("********** Игра Крестики-нолики для двух игроков ********** ")
    play_tic_tac_toe()

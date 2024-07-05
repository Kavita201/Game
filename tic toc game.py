def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True
def get_move(player):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move in '123456789':
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                return row, col
            else:
                print("That spot is already taken. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'
while True:
    print_board(board)
    row, col = get_move(current_player)
    board[row][col] = current_player

    if check_winner(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break
    if check_draw(board):
        print_board(board)
        print("It's a draw!")
        break
    current_player = 'O' if current_player == 'X' else 'X'
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*9)
def check_winner(board,player):
    #Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j]==player for j in range(3)) or all(board[j][i] == player for j in range(3)):
           return True
    if all(board[i][i] == player for i in range(3)) or all (board[i][2 - i]==player for i in range(3)):
       return True
    return False 
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))
def get_empty_position(board):
    return [(i, j) for i in range (3) for j in range(3) if board [i][j] == ' ']
def player_move(board):
    while True:
        try:
            row = int(input("Eneter the row(0,1, or 2): "))
            col = int(input("Eneter the column(0,1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <=2 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move, Please Try again!! ")
        except ValueError:
            print("Invalid input, Please enter a number. ")
def random_agent_move(board):
    empty_positions = get_empty_position(board)
    return random.choice(empty_positions)
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board) 
        if current_player == 'X':
            row, col = player_move(board)
        else:
            print("Agent is making a move!!")
            row, col = random_agent_move(board)
        board[row][col] = current_player 
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins !")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = '0' if current_player == 'X' else 'X'
if __name__=="__main__":
    play_game()
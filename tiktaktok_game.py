def print_board(board):
    print("\n현재 보드:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # 가로, 세로, 대각선 검사
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        try:
            row = int(input(f"플레이어 {current_player}, 행 번호(0-2): "))
            col = int(input(f"플레이어 {current_player}, 열 번호(0-2): "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if row not in range(3) or col not in range(3):
            print("범위는 0~2입니다.")
            continue

        if board[row][col] != " ":
            print("이미 선택된 칸입니다.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"플레이어 {current_player} 승리!")
            break

        if check_draw(board):
            print_board(board)
            print("무승부입니다!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()

N = 8
board = [-1] * N

print(board)

def is_safe(row, col):
    for i in range(row):

        if (board[i] == col):
             return False

        if abs(board[i] - col) == abs(i - row):
             return False

    return True

def solve_problem(row):
    if row == N:
         return True

    for col in range(N):
         if is_safe(row, col):
             board[row] = col

             if solve_problem(row + 1):
                 return True

             board[row] = -1

    return False

if solve_problem(0):
    print("Solutions: ")
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".",end=" ")
        print()
else:
    print("No solution exists")

print(board)

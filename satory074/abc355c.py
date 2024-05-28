N, T = map(int, input().split())
A = list(map(int, input().split()))

is_ana = [[False for _ in range(N)] for _ in range(N)]

row_count = [0] * N
col_count = [0] * N
diag1_count = 0
diag2_count = 0

def check_bingo(row, col):
    # 行、列、斜めのどれかがNになっているかをチェック
    if row_count[row] == N or col_count[col] == N:
        return True
    if diag1_count == N or diag2_count == N:
        return True
    return False

for i, a in enumerate(A):
    a -= 1
    row = a // N
    col = a % N
    
    if not is_ana[row][col]:
        is_ana[row][col] = True
        
        # 行、列、斜めのカウントを更新
        row_count[row] += 1
        col_count[col] += 1
        if row == col:
            diag1_count += 1
        if row == N - 1 - col:
            diag2_count += 1
    
    if check_bingo(row, col):
        print(i + 1)
        break
else:
    print(-1)

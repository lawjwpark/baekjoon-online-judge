from collections import deque

def solution(N, M, board):
    for i in range(N):
        for j in range(M):
            if board[i][j] == "O":
                hole = i, j
            if board[i][j] == "R":
                red = i, j
                board[i][j] = '.'
            if board[i][j] == "B":
                blue = i, j
                board[i][j] = '.'

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque([[red, blue]])
    cnt = 0
    while q:
        r, b = q.popleft()
        cnt += 1
        for i in range(4):
            r_end, b_end = False, False
            while True:
                if r == hole and b == hole:
                    break
                nr = (r[0] + dx[i], r[1] + dy[i])
                nb = (b[0] + dx[i], b[1] + dy[i])
                if r != hole:    
                    if board[nr[0]][nr[1]] == ".":
                        r = nr
                    elif board[nr[0]][nr[1]] == "#":
                        r_end = True
                if b != hole:
                    if board[nb[0]][nb[1]] == ".":
                        b = nb
                    elif board[nb[0]][nb[1]] == "#":
                        b_end = True
                if r_end and b_end:
                    break
            
            if r == hole and b == hole:
                


        
        if r == hole:
            if b == hole:
                return -1
            return cnt

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

print(solution(N, M, board))
from collections import deque
def solution(N, M, board):
    red, blue, hole = [], [], []
    for i in range(N):
        for j in range(M):
            if board[i][j] == "O":
                hole.append(i)
                hole.append(j)
            if board[i][j] == "R":
                red.append(i)
                red.append(j)
                board[i][j] = '.'
            if board[i][j] == "B":
                blue.append(i)
                blue.append(j)
                board[i][j] = '.'
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque([[red, blue, -1]])
    cnt = 0
    while q:
        cnt += 1
        # print(f"cnt {cnt}")
        # print(f"q {q}")
        # print("*" * 10)
        if cnt > 10:
            return -1
        for _ in range(len(q)):
            r, b, dir = q.popleft()
            r_copy, b_copy = r.copy(), b.copy()
            for d in range(4):
                r, b = r_copy.copy(), b_copy.copy()
                if d != dir and (d + 2) % 4 != dir:
                    r_end, b_end = False, False
                    while not (r_end and b_end):
                        nr = [r[0] + dx[d], r[1] + dy[d]]
                        nb = [b[0] + dx[d], b[1] + dy[d]]
                        if not r_end:
                            if board[nr[0]][nr[1]] == "#":
                                r_end = True
                            elif nr == hole:
                                r = hole
                                r_end = True
                            elif nr == b and b_end:
                                r_end = True
                            elif nr != b and board[nr[0]][nr[1]] == ".":
                                r = nr
                        if not b_end:
                            if board[nb[0]][nb[1]] == "#":
                                b_end = True
                            elif nb == hole:
                                b = hole
                                b_end = True
                            elif nb == r and r_end:
                                b_end = True
                            elif nb != r and board[nb[0]][nb[1]] == ".":
                                b = nb
                    
                    if r == hole and b != hole:
                        return cnt
                    
                    if (r != r_copy or b != b_copy) and b != hole:
                        q.append([r, b, d])
    return -1

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

print(solution(N, M, board))
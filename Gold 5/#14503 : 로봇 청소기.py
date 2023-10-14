def solution(N, M, r, c, d, map):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0

    while True:
        if map[r][c] == 0:
            map[r][c] = 2
            cnt += 1
            
        forward = False
        for _ in range(4):
            d = (d - 1) % 4
            nx, ny = r + dx[d], c + dy[d]
            if map[nx][ny] == 0:
                r, c = nx, ny
                forward = True
                break
        if forward:
            continue
        nx, ny = r - dx[d], c - dy[d]
        if map[nx][ny] == 1:
            break
        r, c = nx, ny

    return cnt

N, M = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, M, r, c, d, map))
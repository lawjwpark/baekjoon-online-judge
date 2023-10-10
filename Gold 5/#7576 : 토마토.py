from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
ripe = [(i, j) for i in range(N) for j in range(M) if box[i][j] == 1]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque(ripe)
days = -1

while q:
    days += 1
    for _ in range(len(q)):
        x, y = q.popleft()
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = 1
                q.append((nx, ny))

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()

print(days)
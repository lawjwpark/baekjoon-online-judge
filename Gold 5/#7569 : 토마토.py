from collections import deque

def solution(M, N, H, box):
    ripe = [(k, j, i) for k in range(H) for j in range(N) for i in range(M) if box[k][j][i] == 1]

    q = deque(ripe)
    cnt = -1
    
    while q:
        cnt += 1
        for _ in range(len(q)):
            z, y, x = q.popleft()
            for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                    if box[nz][ny][nx] == 0:
                        box[nz][ny][nx] = 1
                        q.append((nz, ny, nx))
    for k in range(H):
        for j in range(N):
            for i in range(M):
                if box[k][j][i] == 0:
                    return -1

    return cnt

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for j in range(N)] for k in range(H)]

print(solution(M, N, H, box))
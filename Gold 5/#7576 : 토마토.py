# https://www.acmicpc.net/problem/7576

from collections import deque

# 좌표 이동을 위한 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(box, ripe):
    queue = deque(ripe)
    days = -1  # 시작일을 0으로 치지 않고 -1로 초기화
    
    while queue:
        days += 1  # 하루가 지남
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                    box[nx][ny] = 1  # 익은 토마토로 바꿈
                    queue.append((nx, ny))

    # 모든 토마토가 익었는지 확인
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1  # 익지 않은 토마토가 남아있으면 -1 반환
    
    return days

# 입력 받기
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
ripe = [(i, j) for i in range(N) for j in range(M) if box[i][j] == 1]

result = bfs(box, ripe)
print(result)
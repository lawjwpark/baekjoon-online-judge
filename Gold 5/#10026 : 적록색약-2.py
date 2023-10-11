from collections import deque

def solution(N, image):
    def num_group(image):
        def bfs(i, j):
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            q = deque([(i, j)])
            chk[i][j] = 1
    
            while q:
                x, y = q.popleft()
                
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and image[nx][ny] == image[x][y] and not chk[nx][ny]:
                        q.append((nx, ny))
                        chk[nx][ny] = 1
        
        chk = [[0] * N for _ in range(N)]
        cnt = 0
        
        for i in range(N):
            for j in range(N):
                if not chk[i][j]:
                    bfs(i, j)
                    cnt += 1
    
        return cnt

    image2 = [row.replace("G", "R") for row in image]
    print(num_group(image), num_group(image2))

N = int(input())
image = [input() for _ in range(N)]

solution(N, image)
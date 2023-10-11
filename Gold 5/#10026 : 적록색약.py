def solution(N, image):
    def not_checked(chk):
        for i in range(N):
            for j in range(N):
                if not chk[i][j]:
                    return i, j
        return False

    def num_group(image, chk):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        cnt = 0
        
        while not_checked(chk):
            i, j = not_checked(chk)
            stk = [(i, j, image[i][j])]
            while stk:
                x, y, prev_color = stk.pop()
                chk[x][y] = 1
        
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and image[nx][ny] == prev_color and not chk[nx][ny]:
                        stk.append((nx, ny, image[x][y]))
            cnt += 1
                
        return cnt
    
    image1 = image
    image2 = [row.replace("G", "R") for row in image]
    chk1 = [[0] * N for _ in range(N)]
    chk2 = [[0] * N for _ in range(N)]

    print(num_group(image1, chk1), num_group(image2, chk2))

N = int(input())
image = [input() for _ in range(N)]

solution(N, image)
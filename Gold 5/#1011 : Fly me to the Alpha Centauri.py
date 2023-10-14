import math

def solution(T, position):
    dist = [y - x for x, y in position]
    for d in dist:
        sqr = d ** 0.5
        n = math.floor(sqr)
        alpha = sqr - n

        if alpha == 0:
            print(2 * n - 1)
        elif 0 < alpha < 0.5:
            print(2 * n)
        else:
            print(2 * n + 1)

T = int(input())
position = []
for _ in range(T):
    position.append(list(map(int, input().split())))

solution(T, position)
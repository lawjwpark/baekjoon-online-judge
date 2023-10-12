from itertools import combinations

def solution(N, M, map):
    def taxi_dist(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    home_list = [(i, j) for i in range(N) for j in range(N) if map[i][j] == 1]
    chkn_list = [(i, j) for i in range(N) for j in range(N) if map[i][j] == 2]

    table = [[taxi_dist(*home, *chkn) for chkn in chkn_list] for home in home_list]
    min_dist = 130000
    
    for selected in combinations(range(len(chkn_list)), M):
        dist = 0
        for i in range(len(home_list)):
            dist += min([table[i][j] for j in selected])
        min_dist = min(min_dist, dist)
            
    return min_dist

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, map))
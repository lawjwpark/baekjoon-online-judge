def solution(N, S, W):
    def f(eggs, idx):
        eggs_copy = eggs.copy()
        eggs_next_list = []
        
        for i, egg in enumerate(eggs):
            if i != idx and egg[2]:
                eggs_copy[idx][0] -= eggs_copy[i][1]
                eggs_copy[i][0] -= eggs_copy[idx][1]
                
                if eggs_copy[idx][0] <= 0:
                    eggs_copy[idx][2] = 0
                if eggs_copy[i][0] <= 0:
                    eggs_copy[i][2] = 0
                    
                for j in range(idx + 1, N):
                    if eggs_copy[j][2]:
                        eggs_next_list.append(f(eggs_copy, j).copy())
                        break
                    if j == N - 1:
                        eggs_next_list.append(eggs_copy)
            
        if not eggs_next_list:
            return eggs_copy

        print(f"eggs {eggs}\nidx {idx}\neggs_next_list {eggs_next_list}")
        
        max_cnt, max_idx = -1, -1
        for k, eggs_next in enumerate(eggs_next_list):
            cnt = sum([1 - e[2] for e in eggs_next])
            if cnt > max_cnt:
                max_cnt = cnt
                max_idx = k

        return eggs_next_list[max_idx]
    
    eggs = [[S[i], W[i], 1] for i in range(N)]
    eggs_max = f(eggs, 0)
    print(eggs_max)
    
    return sum([1 - egg[2] for egg in eggs_max])
    

N = int(input())
S, W = [], []
for _ in range(N):
    s, w = map(int, input().split())
    S.append(s)
    W.append(w)

print(solution(N, S, W))
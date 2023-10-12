def solution(N, eggs):
    def f(eggs, idx):
        if idx == N:
            result_list.append(sum(1 for e in eggs if e[0] <= 0))
            return
        if eggs[idx][0] <= 0:
            f(eggs, idx + 1)
            return
            
        for i in range(N):
            if i != idx and eggs[i][0] > 0:
                eggs_copy = eggs.copy()
                eggs_copy[idx] = (eggs_copy[idx][0] - eggs_copy[i][1], eggs_copy[idx][1])
                eggs_copy[i] = (eggs_copy[i][0] - eggs_copy[idx][1], eggs_copy[i][1])

                f(eggs_copy, idx + 1)
            elif i == N - 1:
                result_list.append(sum(1 for e in eggs if e[0] <= 0))
        
    result_list = []
    f(eggs, 0)
    
    return max(result_list)

N = int(input())
eggs = []
for _ in range(N):
    S, W = map(int, input().split())
    eggs.append((S, W))

print(solution(N, eggs))
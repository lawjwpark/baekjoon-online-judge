def knapsack(n, k, weights, values):
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(k + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
                
    return dp[n][k]

N, K = map(int, input().split())
weights = []
values = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

print(knapsack(N, K, weights, values))
def knapsack(n, k, weights, values):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, k + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
                
    return dp[n][k]

N, K = map(int, input().split())
weights = []
values = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

print(knapsack(N, K, weights, values))